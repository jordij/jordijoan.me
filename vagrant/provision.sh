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

# You just need this if installing packages from a Git repo
# Set Git repos as known host, in case we have packages to be installed from Github repos
# ssh -T git@github.com -o StrictHostKeyChecking=no

# Install pip dependencies, recursively and in order like a boss
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
            $PIP install $line
        fi
    done < "$1"
}

install_reqs $filename

echo "workon $PROJECT_NAME" >> /home/vagrant/.bashrc

# Set execute permissions on manage.py
chmod a+x $DJANGO_DIR/manage.py

# Create and populate DB (on your virtual machine)
su - vagrant -c "dropdb -Upostgres --if-exists $DB_NAME && \
                createdb -Upostgres $DB_NAME "

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

# Add a couple of aliases to manage.py into .bashrc
cat << EOF >> /home/vagrant/.bashrc
alias djrun="$PYTHON $DJANGO_DIR/manage.py runserver 0.0.0.0:8000"
alias djdev="export PYTHONPATH=${PYTHONPATH}:${PROJECT_DIR} && django-admin.py runserver 0.0.0.0:8000 --settings=${PROJECT_NAME}.settings.dev"
EOF
