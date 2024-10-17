from flask_restx import fields


class AuthRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def signin(self):
        return self.namespace.model('Auth Signin', {
            'username': fields.String(required=True, min_length=3, max_length=80),
            'password': fields.String(required=True, min_length=3, max_length=30)
        })
