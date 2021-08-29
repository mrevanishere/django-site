## Current setup:
1. clone main into /var/www/
2. Install venv and install requirements (and `apt-get install python-dotenv`)

    https://stackoverflow.com/questions/59572174/no-module-named-dotenv-python-3-8/59572201
3. Check server
```
python manage.py check
python manage.py runserver
mkdir static
python manage.py collectstatic
```
4. Add env file
5. Install apache2 and add apache2 configs in conf/apache2 to
```
/etc/apache2/sites-available/<name>.conf
```
5. Add site to apache
```
a2ensite mysite
```
6. `systemctl restart apache2`
Debug extra errors and check logs with
```
LogLevel info
```
at
```
/var/log/apache2/site-error.log
systemctl status apache2.service
```
7. CertBot and restart apache2

    Have to make sure to comment out one of the WSGiDaemonProcess's (known bug) to not have a duplicate. (Comment out the ssl one)


## Container requirements
1. copy or pull site files

    into `/var/www/...`
2. pip install requirements
3. nginx server

    Add this line in `nginx.conf`

```
include /etc/nginx/config.d/*.conf;
```
4. add .env file
5. run server