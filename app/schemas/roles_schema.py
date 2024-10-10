from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.roles_model import RoleModel


class RoleRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Role Create', {
            'name': fields.String(required=True, min_length=3, max_length=30)
        })

    def update(self):
        return self.namespace.model('Role Update', {
            'name': fields.String(min_length=3, max_length=30)
        })


class RoleResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RoleModel
