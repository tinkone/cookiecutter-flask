#!/bin/bash
export FLASK_APP=autoapp.py
export FLASK_DEBUG=1
export APP_CONFG=app.config

export DBNAME=
export DBHOST=localhost
export DBPORT=3306
export DBUSER=
export DBPWD=

export SMTP=smtp.googlemail.com
export MAIL_USERNAME=@gmail.com
export MAIL_PASSWORD=
export DOMAIN='gmail.com'

gunicorn autoapp:app --error-logfile {{cookiecutter.app_name}}-err.log {{cookiecutter.app_name}}--log-file {{cookiecutter.app_name}}-out.log --pid .pid &