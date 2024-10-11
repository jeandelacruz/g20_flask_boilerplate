from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.users_model import UserModel


class UserRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('User Create', {
            'name': fields.String(required=True, min_length=3, max_length=120),
            'last_name': fields.String(required=True, min_length=3, max_length=150),
            'username': fields.String(required=True, min_length=3, max_length=80),
            'password': fields.String(required=True, min_length=3, max_length=30),
            'email': fields.String(required=True, min_length=3, max_length=160),
            'rol_id': fields.Integer(required=True)
        })

    def update(self):
        return self.namespace.model('User Update', {
            'name': fields.String(required=False, min_length=3, max_length=120),
            'last_name': fields.String(required=False, min_length=3, max_length=150),
            'username': fields.String(required=False, min_length=3, max_length=80),
            'email': fields.String(required=False, min_length=3, max_length=160),
            'rol_id': fields.Integer(required=False)
        })


class UserResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        exclude = ['password']
        include_fk = True

    role = Nested('RoleResponseSchema', many=False)
