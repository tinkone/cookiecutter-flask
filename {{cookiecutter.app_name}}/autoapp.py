# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag
from flask_script import Manager

from {{cookiecutter.app_name}}.app import create_app, init_db
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

manager = Manager(app)
# manager.add_option('-i', '--ini', dest='ini', required=False)
@manager.command
def seed():
    print("seed database lookup tables")
    init_db()


if __name__ == '__main__':
    manager.run()