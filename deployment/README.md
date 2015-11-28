Deploy
------

`deploy.sh` and `post_deploy.sh` are intended to be used in **production only**. You should place them under your user home directory, something like `/var/www/myuser/`.

Both scripts are supposed to be executed through our Codeship deployment/production instance **only**. The Codeship configuration for deployment purposes:

```
$ rsync -avz -e ssh ~/clone/ myuser@mydomain.co.nz:/var/www/myuser/mydomain.co.nz/myuser/
$ ssh myuser@mydomain.co.nz './deploy.sh myuser mydomain.co.nz myuser.settings.production'
$ ssh myuser@mydomain.co.nz 'sudo ./post_deploy.sh'
```

The `post_deploy.sh` should be owner by root. This line `nzoty ALL=NOPASSWD: /var/www/myuser/post_deploy.sh` should be pasted into:

```
$ nano /etc/sudoers.d/myuser
```

So **myuser** can execute it.


**You should get rid of this folder as it's not relevant for development.**