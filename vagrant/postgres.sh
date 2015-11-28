#!/bin/bash

# Let us connect to the database from our local machine to the vagrant machine without credentials
echo -n 'Updating pg_hba.conf ...'
su - vagrant -c "sudo sed -i '$ a host all all 10.0.2.2/24 trust' /etc/postgresql/9.3/main/pg_hba.conf"
su - vagrant -c "sudo sed -i 's/local\s\{1,\}all\s\{1,\}postgres\s\{1,\}peer/local all postgres trust/g' /etc/postgresql/9.3/main/pg_hba.conf"
echo -n 'Updating postgresql.conf ... '
su - vagrant -c "sudo perl -pi -e \"s/#listen_addresses = 'localhost'/listen_addresses = '*'/g\" /etc/postgresql/9.3/main/postgresql.conf "
su - vagrant -c "sudo service postgresql restart"