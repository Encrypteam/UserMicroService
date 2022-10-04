import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_consulate import Consul
import pymysql
from prometheus_flask_exporter import PrometheusMetrics

pymysql.install_as_MySQLdb()

consul = Consul(max_tries=25)
db = SQLAlchemy()
metrics = PrometheusMetrics.for_app_factory()
metrics.info('users', 'Description', version='0.1')


def create_app():
    app = Flask(__name__)
    metrics.init_app(app)
    consul.init_app(app)
    consul.register_service(
        name='user-ms',
        interval='10s',
        tags=[''],
        httpcheck='https://users.encrypteam.localhost/healthcheck'
    )
    consul.apply_remote_config(namespace='configuration/users/')
    load_dotenv()

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + os.getenv('DATABASE_USER') + ':' + os.getenv(
        'DATABASE_PASSWORD') + '@' + os.getenv('DATABASE_URL') + ':' + os.getenv('DATABASE_PORT') + '/' + os.getenv(
        'DATABASE_NAME')
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + app.config['users']['DATABASE_USER'] + ':' + app.config['users']['DATABASE_PASSWORD'] + '@' + app.config['users']['DATABASE_URL'] + ':' + app.config['users']['DATABASE_PORT'] + '/' + app.config['users']['DATABASE_NAME']

    db.init_app(app)
    from main.resources import home
    from main.resources import users

    app.register_blueprint(home)
    app.register_blueprint(users, url_prefix='/users')
    return app

