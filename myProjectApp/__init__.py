# __init__.py file underneath myProjectApp folder
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import *
from .auth import *
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
# DB_NAME = "database.db"


basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'this is a secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    # app.config['SQLALCHEMY_DATABASE_URI'] = sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Tracker, Log

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + 'data.sqlite'):
        db.create_all(app=app)
        print('Created Database!')
