from marshmallow import Schema, fields, validate, post_load
from main.models import User


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True, validate=validate.Length(min=3, max=50))
    key = fields.String(required=True, validate=validate.Length(min=1, max=120))

    @post_load
    def make_user(self, data):
        return User(**data)
