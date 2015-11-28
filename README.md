
jordijoan.me
==================

[ Put your ASCII art in here ]

Basic Wagtail-based project setup. All of our Wagtail-based project should be started on top of this.

# Installation

Install Vagrant and  VirtualBox:

* [Vagrant](http://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

# Setup

## Basic setup

```
  $ cd [my-dev-environment]
  $ git clone git@github.com:springload/jordijoan.me.git
  $ cd jordijoan.me
  $ vagrant up
  [..... wait until everything gets installed]
  $ vagrant ssh
  $ djdev
```

You're done, **you hero**! Your instance is up and running! Available on **http://localhost:8111**

## PostgreSQL setup

If your project is going to use PostgrSQL you should probably follow these guidelines:

As a PostgreSQL client you should install [PgAdmin](http://www.pgadmin.org/download/) Setup a localhost connection with the forwarded 15432 port.

To init your project DB:

1. Define your initials models and snippets (`core/models.py`, `core/snippets.py`)
2. Create a new DB for your project:
    * `createdb -Upostgres your_db_name`
2. Edit your DB settings in the Django settings file to be pointing to your DB
4. Make your initial migration and run it:
    * `$ ./manage.py makemigrations`
    * `$ ./manage.py syncdb`
5. Uncomment the following lines from the `vagrant/provision.sh` file:
```
    su - vagrant -c "$PYTHON $PROJECT_DIR/manage.py migrate --noinput && \
                $PYTHON $PROJECT_DIR/manage.py load_initial_data && \
                $PYTHON $PROJECT_DIR/manage.py update_index"
```

If you need to generate new fixtures, I recommend you running the ultimate mofo command:

```
  ./manage.py dumpdata --indent=4 -e contenttypes -e auth.permission -e auth.group -e sessions -e wagtailcore.site -e wagtailcore.pagerevision -e wagtailcore.grouppagepermission -e wagtailimages.filter -e wagtailimages.rendition --natural-primary --natural-foreign > initial_data.json
```

If you want, **tweak the dumped fixtures** to make sure your pages pks start from **1** onwards.

Finally do your **tests** and commit your changes so the rest of the team can enjoy your work!

If you want to be able to connect to the PostgreSQL server in your Vagrant machine you need to edit a couple of settings. Edit `/etc/postgresql/x.x/main/postgresql.conf` in the Vagrant machine and be sure you have something similar in the following line:

```
listen_addresses = '*'          # what IP address(es) to listen on;
```

Then edit `/etc/postgresql/9.3/main/pg_hba.conf` (also in the Vagrant machine) and check you have something like this at the end of the file:

```
# Database administrative login by UNIX sockets
local   all         postgres                          trust

# TYPE  DATABASE    USER        CIDR-ADDRESS          METHOD
local   all         all                               trust
host    all         all            10.0.2.2/24           trust
host    all         all         127.0.0.1/32          trust
```

## Media folder synced to a Delila preview site

Edit the `Vagrantfile` and uncomment the following line:

```
config.vm.synced_folder "/Volumes/Preview Sites/" + PROJECT_NAME + "/media/", "/home/vagrant/" + PROJECT_NAME + "/media" 
```

Your path to the mounted folder might be different, just edit the first argument according to it.

Now edit the `jordijoan.me/settings/base.py` and uncomment the following line:

```
# MEDIA_ROOT = join(PROJECT_ROOT, WAGTAIL_SITE_NAME.lower(), 'media')
```

Restart vagrant check it's working. If you get an error while runnning `vagrant up` like this:

![Mounted volume error](http://i.imgur.com/0SXZ0ff.png)

Just make sure the preview sites folder is properly mounted in your host machine. In MacOS it is usally not unless you open the folder with Finder.

If you want to run the server using the delila settings (database mostly) use:

```
  $ djrun
```

## Tips

If you're not in the office or you don't have access to the VagrantBox, try to change the link in the `Vagrantfile`:
```
config.vm.box_url = "https://www.dropbox.com/s/e229abqxjkeaj8o/wagtail-base-v0.3.box?dl=1"

```

If at some point you want to restore your pre-cooked DB, run your vagrant forcing the provision:

```
  $ vagrant up --provision
```

# Deployment setup

Check our guidelines on [deployment](./deployment/README.md)
