# Days 89 - 92 Deploying web applications on Linux

In this your-turn, you will deploy one of the web apps that you have created during this course.

## Day 1: Watch the video lessons

The first day of this 4-day block is to watch the videos. There is a lot of content here but we want to spend one day per type of test for the remaining three days so try to get through it in one here.

## Day 2: Create and patch the linux server 

To create the Ubuntu 18.04 server, you have a few options. Just pick one that works best for you and go with that. Remember that after the server is created it's all the same.

Where to host your server? If you use the links below, you'll get a small or medium credit on top of just regularly signing up.

1. **Digital Ocean**: Use [**pythonbytes.fm/digitalocean**](https://pythonbytes.fm/digitalocean) and get $100 credit for new accounts
2. **Linode**: Use [**talkpython.fm/linode**](https://talkpython.fm/linode) and get $20 credit (all users I believe)
3. **Amazon Lightsail**: [**aws.amazon.com/lightsail**](https://aws.amazon.com/lightsail/)
4. **Local VM**: If you use something like VMWare, Parallels, or VirtualBox, you can just create a local Ubuntu if you'd rather

If you decide to use EC2 directly, remember they put a firewall in front of your server which blocks port 80 be default. You'll have to allow that in the EC2 console in addition to anything you do in Ubuntu.

Create the server, log in, and immediately patch it using the three commands:

```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo reboot
```

You'll need to use SSH to access the server most likely. On macOS, Windows, and Linux, `ssh` is built in. On Windows, you have a few options.

* Use cmd.net. This is an awesome command prompt replacement: **[cmder.net](http://cmder.net/)**
* Use PowerShell: This is built into Windows and has SSH capabilities

## Day 3: Get your site running under uWSGI

### Software dependencies

Once your server is setup and you've logged in successfully, you'll want to install the necessary software dependencies to run Python 3 and uWSGI.

You can use the script I used during the demos to guide you through this. You can find the script in the `server` folder here:

[https://github.com/talkpython/100daysofweb-with-python-course/tree/master/days/089-092-deployment/demo/billtracker/server](https://github.com/talkpython/100daysofweb-with-python-course/tree/master/days/089-092-deployment/demo/billtracker/server). 

Here are the relevant commands for your convenience:

```bash
# Install some OS dependencies:
$ sudo apt install -y -q build-essential git
$ sudo apt install -y -q python3-pip python3-dev python3-venv
# for gzip support in uwsgi
$ sudo apt install --no-install-recommends -y -q libpcre3-dev libz-dev
$ sudo apt install -y -q nginx
$ sudo apt install -y nload

# Stop the hackers
$ sudo apt install fail2ban -y

$ ufw allow ssh
$ ufw allow http
$ ufw allow https
$ ufw enable

# Basic git setup
$ git config --global credential.helper 'cache --timeout=720000'

# Be sure to put your info here:
$ git config --global user.email "you@email.com"
$ git config --global user.name "Your name"
```

Run through the commands one at a time to see what they do. Of course, substitute your contact info in GitHub.

### Source code for the web app

Once the server is ready to run Python 3, you'll need to get your source code on the server. Here you will need to decide what code to publish! If you are feeling adventurous, pick one of the apps you've created throughout this course and get it online. 

If you'd rather play it safe the first time around, we've included a working copy of bill tracker here:

[https://github.com/talkpython/100daysofweb-with-python-course/tree/master/days/089-092-deployment/demo/billtracker](https://github.com/talkpython/100daysofweb-with-python-course/tree/master/days/089-092-deployment/demo/billtracker)

This just the one from the demo that we used in the videos. 

Use these steps to prepare the file structure on the server:

```bash
# Web app file structure

$ mkdir /webapps
$ chmod 777 /webapps
$ mkdir /webapps/logs
$ mkdir /webapps/logs/billtracker
$ mkdir /webapps/logs/billtracker/app_log
$ cd /webapps

# Create a virtual env for the app.

$ cd /webapps
$ python3 -m venv venv
$ source /webapps/venv/bin/activate
(venv) $ pip install --upgrade pip setuptools
(venv) $ pip install --upgrade httpie glances
(venv) $ pip install --upgrade uwsgi
```

Now to get the source code here, use this command (substitute your repo path if you are using a different app):

```
# clone the repo:
(venv) $ cd /webapps
(venv) $ git clone https://github.com/talkpython/100daysofweb-with-python-course app_repo

# Setup the web app:
(venv) $ cd /webapps/app_repo/days/089-092-deployment/demo/billtracker/
(venv) $ pip install -r requirements.txt
(venv) $ python setup.py develop
```

If you deployed bill tracker, you can test it with the command:

```
(venv) $ cd /webapps/app_repo/days/089-092-deployment/demo/billtracker/
(venv) $ pserve development.ini 
```

In a new terminal, you can log in and try to hit the site:

```
(venv) $ http http://localhost:6543/
```

### Running under uWSGI

Finally, to get it running in uWSGI, let's test it with:

```
(venv) $ /webapps/venv/bin/uwsgi -H /webapps/venv --ini-paste /webapps/app_repo/days/089-092-deployment/demo/billtracker/production.ini
```

Remember if you are deploying another app you've built, you'll need to specify the uWSGI config info (in `production.ini` for Pyramid, creating a `uwsgi.ini` file for Django, or following along with the Flask docs).

Once this is all working, you're ready to setup this server to run uWSGI automatically. Just copy the service file as follows:

```bash
# Copy and enable the daemon

$ cp /webapps/app_repo/days/089-092-deployment/demo/billtracker/server/billtracker.service /etc/systemd/system/billtracker.service
```

Be sure to review the contents of `billtracker.service` to make sure you understand what it does.

Then enable and start the service:

```bash
$ systemctl start billtracker
$ systemctl status billtracker
$ systemctl enable billtracker
```

Reboot the server (just type `reboot`) and verify the site is running internally by logging back in, activate the virtual environment, and running `http localhost:9055`.

## Day 4: Publish the site via nginx

You're in the home stretch now. Just need to get your site running on the public web server (nginx). Here are the few steps needed:

```bash
# Setup the public facing server (NGINX)

# CAREFUL HERE. If you are using default, maybe skip this
$ rm /etc/nginx/sites-enabled/default

$ cp /webapps/app_repo/days/089-092-deployment/demo/billtracker/server/billtracker.nginx /etc/nginx/sites-enabled/billtracker.nginx

$ update-rc.d nginx enable

$ service nginx restart
```

Be sure to review the contents of `billtracker.nginx` to make sure you understand what it does.

Now is the moment of truth. Try to access the service:

```
(venv) $ http localhost
```

If you see your HTML source, you've done it! If not, start looking at the error messages and logs. They are usually found in `/var/log` or `/var/log/nginx` for nginx and `/webapps/logs/billtracker/uwsgi.log` for uWSGI.

Finally, try to access the site from outside the server in your browser. Just type the ip address into the address bar of your browser and you should see your site if all is well!

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*


