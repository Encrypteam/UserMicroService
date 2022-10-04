from flask import Blueprint, jsonify
from main import metrics

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    return jsonify('This is the home'), 200


@metrics.summary('request_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@home.route('/healthcheck')
def healthcheck():
    return jsonify({'status': 'up'}), 200
