"""
Usage:

 $ fab help

"""

from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env, put
from fabric.operations import sudo

from fabric.contrib.project import rsync_project

import os
# import re
# import sys
# import time

env.use_ssh_config = True
env.timeout = 5
env.keepalive = 25  # SSH keepalive interval
env.user_home = os.getenv('HOME')
env.user = 'ubuntu'
env.password = ''
env.hosts=['']
env.key_filename = '~/.ssh/.pem'


def update():
    sudo('apt-get update -y')

def apache():
    sudo('apt-get install apache2 -y')

def tmux():
    sudo('apt-get install tmux -y')
    #copy config out

def mariadb():
    sudo("apt-get install software-properties-common")
    sudo("apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8")
    sudo("add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mirror.jmu.edu/pub/mariadb/repo/10.1/ubuntu xenial main'")
    update()
    sudo("apt-get install -y mysql-client libmysqlclient-dev mariadb-server")

def py():
    sudo("apt-get install python3 python-pip python-dev libapache2-mod-wsgi -y")
    sudo("pip install virtualenv flask")
    sudo("pip install --upgrade")




def ebs():
    sudo("mkdir /vol")
    sudo("mkfs -t ext4 /dev/xvdb")
    sudo('mv /var/lib/mysql /vol')
    sudo("ln -s /vol/mysql /var/lib/mysql")
    sudo("ln -s /vol/images /var/www/images")

def keys():
    sudo("ln -s /vol/keys/ubuntu/.ssh /home/ubuntu/.ssh")
    sudo("ln -s /vol/keys/root/.ssh /root/.ssh")

def setup_app(pull=False):
    # cd("~")

    # cd("zeus")
    if pull is True:
        with cd("/vol"):
            sudo("git clone ")
        # sudo("chmod -R 777 .")
        # sudo("chown -R `whoami`:`whoami` .")
    with cd("/vol/zeus"):
        sudo("virtualenv venv -p /usr/bin/python3.5")
        sudo("source venv/bin/activate")
        sudo("pip install -r ./requirements.txt")
        sudo("source ./start.sh")

def certbot():
    sudo("add-apt-repository ppa:certbot/certbot")
    update()
    sudo("apt-get install certbot python-certbot-apache -y")


def start():
    with cd("/vol/zeus"):
        run(". ./start.sh")
        
def deploy():
    with cd("/vol/zeus"):
        with settings(warn_only=True):
            run("./stop.sh")
            run("git reset --hard HEAD && git pull origin master")
            # run("git pull origin master")
            import time
            time.sleep(3)
            put("start.sh", "/vol/zeus", use_sudo=True)
            run(". ./start.sh")

def robots():
    put("robots.txt", "/var/www/html", use_sudo=True)

def home():
    put("index.html", "/var/www/html",use_sudo=True)

def jail():
    put("jail.conf", "/etc/fail2ban", use_sudo=True)

def marketing():
    rsync_project("/var/www/html/", "./marketing/html/*")


def setup():
    # update()
    # apache()
    # tmux()
    # mariadb()
    # py()
    # ebs()
    # keys()
    setup_app()
