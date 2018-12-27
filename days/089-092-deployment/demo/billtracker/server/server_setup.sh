#!/usr/bin/env bash

# Consider running these two commands separately
# Do a reboot before continuing.
apt update
apt upgrade -y

# Install some OS dependencies:
sudo apt install -y -q build-essential git
sudo apt install -y -q python3-pip python3-dev python3-venv
# for gzip support in uwsgi
sudo apt install --no-install-recommends -y -q libpcre3-dev libz-dev
sudo apt install -y -q nginx
sudo apt install -y nload

# Stop the hackers
sudo apt install fail2ban -y

ufw allow ssh
ufw allow http
ufw allow https
ufw enable

# Basic git setup
git config --global credential.helper 'cache --timeout=720000'

# Be sure to put your info here:
git config --global user.email "you@email.com"
git config --global user.name "Your name"

# Web app file structure
mkdir /webapps
chmod 777 /webapps
mkdir /webapps/logs
mkdir /webapps/logs/billtracker
mkdir /webapps/logs/billtracker/app_log
cd /webapps

# Create a virtual env for the app.
cd /webapps
python3 -m venv venv
source /webapps/venv/bin/activate
pip install --upgrade pip setuptools
pip install --upgrade httpie glances
pip install --upgrade uwsgi


# clone the repo:
cd /webapps
git clone https://github.com/talkpython/100daysofweb-with-python-course app_repo

# Setup the web app:
cd /webapps/app_repo/days/089-092-deployment/demo/billtracker/
pip install -r requirements.txt
python setup.py develop


# Copy and enable the daemon
cp /webapps/app_repo/days/089-092-deployment/demo/billtracker/server/billtracker.service /etc/systemd/system/billtracker.service

systemctl start billtracker
systemctl status billtracker
systemctl enable billtracker

# Setup the public facing server (NGINX)

# CAREFUL HERE. If you are using default, maybe skip this
rm /etc/nginx/sites-enabled/default

cp /webapps/app_repo/days/089-092-deployment/demo/billtracker/server/billtracker.nginx /etc/nginx/sites-enabled/billtracker.nginx
update-rc.d nginx enable
service nginx restart
