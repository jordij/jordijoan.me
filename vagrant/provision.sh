#!/bin/bash

PROJECT_NAME=$1
REQUIREMENTS_FILE=$2

DB_NAME=$PROJECT_NAME
PROJECT_DIR=/home/vagrant/$PROJECT_NAME
DJANGO_DIR=$PROJECT_DIR
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

PYTHON=$VIRTUALENV_DIR/bin/python
PIP=$VIRTUALENV_DIR/bin/pip

# Virtualenv setup for project
su - vagrant -c "/usr/local/bin/virtualenv $VIRTUALENV_DIR && \
    echo $PROJECT_DIR > $VIRTUALENV_DIR/.project && \
    PIP_DOWNLOAD_CACHE=/home/vagrant/.pip_download_cache "

# Install pip dependencies, recursively and in order
filename="$PROJECT_DIR/$REQUIREMENTS_FILE"

install_reqs()
{
    while read -r line || [[ -n $line ]]
    do
        if [[ -n "$line" && "$line" =~ ^\-r ]];then
            for word in $line; do
                echo $word
            done
            echo "INSTALLING file $word"
            install_reqs "$PROJECT_DIR/requirements/$word"
        elif [[ -n "$line" && "$line" != [[:blank:]#]* ]];then
            echo "INSTALLING package $line"
            su - vagrant -c "$PIP install $line"
        fi
    done < "$1"
}

pip install -r $filename

# Set execute permissions on manage.py
chmod a+x $DJANGO_DIR/manage.py

# Create and populate DB (on your virtual machine)
su - vagrant -c "dropdb --if-exists $DB_NAME && \
                createdb $DB_NAME"

# Run migrate/update_index/load_initial_data
su - vagrant -c "$PYTHON $PROJECT_DIR/manage.py migrate --noinput && \
                 $PYTHON $PROJECT_DIR/manage.py load_initial_data && \
                 $PYTHON $PROJECT_DIR/manage.py update_index"

# Create static folder if necessary
if test -d $PROJECT_DIR/static; then
    echo "static folder exists"
else
    su - vagrant -c "mkdir $PROJECT_DIR/static"
fi

# Add an alias to manage.py into .bashrc
cat << EOF >> /home/vagrant/.bashrc
alias djrun="$PYTHON $DJANGO_DIR/manage.py runserver 0.0.0.0:8000"

source $VIRTUALENV_DIR/bin/activate
export PS1="[$PROJECT_NAME \W]\\$ "
cd $PROJECT_DIR
EOF