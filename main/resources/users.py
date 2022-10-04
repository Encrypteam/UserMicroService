from flask import Blueprint, request, jsonify
from main.services import UserService
from main.map import UserSchema
from main import metrics

users = Blueprint('users', __name__)

user_schema = UserSchema()


@users.route('/', methods=['POST'])
def create():
    service = UserService()
    user = user_schema.load(request.get_json())
    return user_schema.dump(service.create(user))

@metrics.counter('Users by name', 'Number of users by name',
                 labels={'item': lambda: request.view_args['username']})
@users.route('/username/<username>', methods=['GET'])
def find_by_username(username):
    service = UserService()
    if service.find_by_username(username) is None:
        return jsonify('User not found'), 404
    return jsonify(user_schema.dump(service.find_by_username(username))), 200


@users.route('/id/<id>', methods=['GET'])
def find_by_id(id):
    service = UserService()
    return user_schema.dump(service.find_by_id(id))


@users.route('/all', methods=['GET'])
def find_all():
    service = UserService()
    return jsonify(user_schema.dump(service.find_all(), many=True)), 200


@users.route('/update', methods=['PUT'])
def update():
    service = UserService()
    user = user_schema.load(request.get_json())
    return user_schema.dump(service.update(user))
