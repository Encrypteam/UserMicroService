import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + os.getenv('DATABASE_USER') + ':' + os.getenv(
        'DATABASE_PASSWORD') + '@' + os.getenv('DATABASE_URL') + ':' + os.getenv('DATABASE_PORT') + '/' + os.getenv(
        'DATABASE_NAME')
    db.init_app(app)
    from main.resources import home

    app.register_blueprint(home, url_prefix='/api/v1')
    app.register_blueprint(user, url_prefix='/api/v1/users')
    return app

