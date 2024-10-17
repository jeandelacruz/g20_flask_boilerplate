from flask_restx import fields
from flask_restx.reqparse import RequestParser


class AuthRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def signin(self):
        return self.namespace.model('Auth Signin', {
            'username': fields.String(required=True, min_length=3, max_length=80),
            'password': fields.String(required=True, min_length=3, max_length=30)
        })

    def refresh_token(self):
        parser = RequestParser()
        parser.add_argument('Authorization', type=str,
                            location='headers', help='Ex: Bearer {token}')
        return parser

    def password_reset(self):
        return self.namespace.model('Auth Password Reset', {
            'email': fields.String(required=True)
        })
