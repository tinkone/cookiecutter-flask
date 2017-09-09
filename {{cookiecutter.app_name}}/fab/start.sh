#!/bin/bash
export FLASK_APP=autoapp.py
export FLASK_DEBUG=0
export APP_CONFG=app.config

export DBNAME=
export DBHOST=localhost
export DBPORT=3306
export DBUSER=
export DBPWD=

export SMTP=
export MAIL_USERNAME=
export MAIL_PASSWORD=
export DOMAIN=

gunicorn autoapp:app --error-logfile {{cookiecutter.app_name}}-err.log --log-file {{cookiecutter.app_name}}-out.log --pid {{cookiecutter.app_name}}.pid &