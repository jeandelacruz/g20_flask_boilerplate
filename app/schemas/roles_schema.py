from flask_restx import fields


class RoleRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Role Create', {
            'name': fields.String(required=True, min_length=3, max_length=30)
        })
