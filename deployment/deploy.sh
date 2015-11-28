#!/bin/bash

# This script needs the following 3 parameters to work properly: USERNAME, DOMAIN, SETTINGS
# Example:
# $ ./deploy.sh buildability buildability.co.nz buildability.settings.production
# It could be improved but it's a starting point

USERNAME=$1
DOMAIN=$2
SETTINGS=$3

# Activate virtual environment
source /var/www/$USERNAME/venvs/$DOMAIN/bin/activate
cd /var/www/$USERNAME/$DOMAIN/$USERNAME

# Install requirements in case there are new dependencies or updates
if [ -f requirements/production.txt ]; then
    pip install -r requirements/production.txt
fi

# Check for migrations
output="$(./manage.py migrate --settings=${SETTINGS}  --list | grep "\[ ]" | wc -l)"

if [ $output -ge 1 ]
then
  ./manage.py migrate --settings=$SETTINGS
else
  echo "No migrations to run"
fi

# A bit of clean-up tasks
./manage.py collectstatic --noinput --settings=$SETTINGS
./manage.py compress --settings=$SETTINGS
./manage.py update_index --settings=$SETTINGS

deactivate
