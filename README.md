[ ![Codeship Status for jordij/jordi.nz](https://codeship.com/projects/3f0d2bc0-829a-0133-5908-5a5099820553/status?branch=master)](https://codeship.com/projects/121639)

# DISCLAIMER: Python 2.7 based code, use at your own risk


Site/blog living on [https://jordi.nz](https://jordi.nz)

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
  $ djrun
```
Generate assets:
```
  $ cd core/static
  $ sass sass/main.scss > css/main.css
```

The site should be Available on **http://localhost:8111** Admin credentials are admin-admin. You'll need to edit the site (Settings -> Sites) and change the homepage as it comes with the "Welcome to your new Wagtail site!" page by default.