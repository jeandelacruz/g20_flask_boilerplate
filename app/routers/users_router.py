from app import api
from flask import request
from flask_restx import Resource
from app.controllers.users_controller import UserController


user_ns = api.namespace(
    name='Users',
    description='Endpoints del modulo Users',
    path='/users'
)


@user_ns.route('')
class UsersListCreate(Resource):
    def get(self):
        ''' Listar todos los usuarios '''
        controller = UserController()
        return controller.fetch_all()

    def post(self):
        ''' Creacion de un usuario '''
        pass


@user_ns.route('/<int:id>')
class UsersGetUpdateDelete(Resource):
    def get(self, id):
        ''' Obtener un usuario por su id '''
        pass

    def patch(self, id):
        ''' Actualizar un usuario por su id '''
        pass

    def delete(self, id):
        ''' Eliminar un usuario por su id '''
        pass
