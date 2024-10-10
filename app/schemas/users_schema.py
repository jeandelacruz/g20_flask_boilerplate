from flask_restx import fields


class UserRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('User Create', {
            'name': fields.String(required=True, min_length=3, max_length=120),
            'last_name': fields.String(required=True, min_length=3, max_length=150),
            'username': fields.String(required=True, min_length=3, max_length=80),
            'password': fields.String(required=True, min_length=3, max_length=30),
            'email': fields.String(required=True, min_length=3, max_length=160),
            'rol_id': fields.Integer(required=True)
        })
