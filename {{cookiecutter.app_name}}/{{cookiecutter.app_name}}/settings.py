# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('{{cookiecutter.app_name | upper}}_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    DBNAME = os.environ.get('DBNAME', '')
    DBHOST = os.environ.get('DBHOST', '')
    DBPORT = 3306
    DBUSER = os.environ.get('DBUSER', '')
    DBPWD = os.environ.get('DBPWD', '')
    DBURL = 'mysql://{DBUSER}:{DBPWD}@{DBHOST}:{DBPORT}/{DBNAME}'.format(**locals())
    # Put the db file in project root

    DB_PATH = os.path.join(Config.PROJECT_ROOT, DBNAME)

    SQLALCHEMY_DATABASE_URI = DBURL
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_POOL_SIZE = 20

    MAIL_SERVER = os.environ.get('SMTP')
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['donotreply@' + os.environ.get('DOMAIN', '')]

    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True

    DBNAME = 'dev.db'
    DBHOST = '0.0.0.0'
    DBPORT = 3306
    DBUSER = 'developer'
    DBPWD = 'xxx'
    DBURL = 'mysql://{DBUSER}:{DBPWD}@{DBHOST}:{DBPORT}/{DBNAME}'.format(**locals())
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DBNAME)

    SQLALCHEMY_DATABASE_URI = DBURL

    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.

    # email server
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['@gmail.com']


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
