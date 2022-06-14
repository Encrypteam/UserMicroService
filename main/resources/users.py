from flask import Blueprint, request
from main.services import UserService
from main.map import UserSchema


users = Blueprint('users', __name__)

user_schema = UserSchema()


@users.route('/', methods=['POST'])
def create():
    service = UserService()
    user = user_schema.load(request.get_json())
    return user_schema.dump(service.create(user))


@users.route('/username/<username>', methods=['GET'])
def find_by_username(username):
    service = UserService()
    return user_schema.dump(service.find_by_username(username))


@users.route('/id/<id>', methods=['GET'])
def find_by_id(id):
    service = UserService()
    return user_schema.dump(service.find_by_id(id))


@users.route('/all', methods=['GET'])
def find_all():
    service = UserService()
    return user_schema.dump(service.find_all())


@users.route('/update', methods=['PUT'])
def update():
    service = UserService()
    user = user_schema.load(request.get_json())
    return user_schema.dump(service.update(user))
