#!/usr/bin/python3
#  sets up your web servers for the deployment of web_static.

#installing Nginx
apt-get update
apt-get install nginx -y

#create a folder 
mkdir -p data/web_static/releases/test/
mkdir -p /data/web_static/shared/

#create a fake HTML file
echo "Holberton School" > /data/web_static/releases/test/index.html

#create a symbolic link /data/web_static/current linked to folder
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ folder to ubuntu user and group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# update nginx config and restart use alias
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# restart server
service nginx restart
