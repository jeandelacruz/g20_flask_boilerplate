from app import api
from flask import request
from flask_restx import Resource
from app.controllers.users_controller import UserController
from app.schemas.users_schema import UserRequestSchema


user_ns = api.namespace(
    name='Users',
    description='Endpoints del modulo Users',
    path='/users'
)

request_schema = UserRequestSchema(user_ns)


@user_ns.route('')
class UsersListCreate(Resource):
    def get(self):
        ''' Listar todos los usuarios '''
        controller = UserController()
        return controller.fetch_all()

    @user_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creacion de un usuario '''
        controller = UserController()
        return controller.save(request.json)


@user_ns.route('/<int:id>')
class UsersGetUpdateDelete(Resource):
    def get(self, id):
        ''' Obtener un usuario por su id '''
        controller = UserController()
        return controller.find_by_id(id)

    @user_ns.expect(request_schema.update(), validate=True)
    def patch(self, id):
        ''' Actualizar un usuario por su id '''
        controller = UserController()
        return controller.update(id, request.json)

    def delete(self, id):
        ''' Eliminar un usuario por su id '''
        controller = UserController()
        return controller.remove(id)
