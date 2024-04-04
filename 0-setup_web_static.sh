#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.

# installing Nginx
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'

#create a folder
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#create a fake HTML file
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#create a symbolic link /data/web_static/current linked to folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update nginx config and restart use alias
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart
sudo service nginx restart
