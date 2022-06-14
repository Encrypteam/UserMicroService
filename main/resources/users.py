from flask import Blueprint, request
from main.services import UserService

home = Blueprint('home', __name__)

user_schema = UserSchema()


@home.route('/', methods=['POST'])
def create():
    service = UserService()
    user = user_schema.load(request.get_json())
    return user_schema.dump(service.create(user))


@home.route('/username/<username>', methods=['GET'])
def find_by_username(username):
    service = UserService()
    return user_schema.dump(service.find_by_username(username))


@home.route('/id/<id>', methods=['GET'])
def find_by_id(id):
    service = UserService()
    return user_schema.dump(service.find_by_id(id))


@home.route('/all', methods=['GET'])
def find_all():
    service = UserService()
    return user_schema.dump(service.find_all())


@home.route('/update', methods=['PUT'])
def update():
    service = UserService()
    user = user_schema.load(request.get_json())
    return user_schema.dump(service.update(user))
