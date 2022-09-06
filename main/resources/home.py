from flask import Blueprint, jsonify

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    return jsonify('This is the home'), 200


@home.route('/healthcheck')
def healthcheck():
    return jsonify({'status': 'up'}), 200
