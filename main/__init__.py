import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_consulate import Consul
import pymysql
pymysql.install_as_MySQLdb()

consul = Consul(max_tries=10)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    consul.init_app(app)
    consul.register_service(
        name='user-ms',
        interval='10s',
        tags=[''],
        httpcheck='https://users.encrypteam.localhost/healthcheck'
    )
    consul.apply_remote_config(namespace='configuration/users/')
    load_dotenv()
    print("CONFIG DE CONSUL", app.config['users'])

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + os.getenv('DATABASE_USER') + ':' + os.getenv(
    #    'DATABASE_PASSWORD') + '@' + os.getenv('DATABASE_URL') + ':' + os.getenv('DATABASE_PORT') + '/' + os.getenv(
    #    'DATABASE_NAME')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + app.config['users']['DATABASE_USER'] + ':' + app.config['users']['DATABASE_PASSWORD'] + '@' + app.config['users']['DATABASE_URL'] + ':' + app.config['users']['DATABASE_PORT'] + '/' + app.config['users']['DATABASE_NAME']

    db.init_app(app)
    from main.resources import home
    from main.resources import users

    app.register_blueprint(home, url_prefix='/api/v1')
    app.register_blueprint(users, url_prefix='/api/v1/users')
    return app

