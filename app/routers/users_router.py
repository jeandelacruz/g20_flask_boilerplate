from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.controllers.users_controller import UserController
from app.schemas.users_schema import UserRequestSchema


user_ns = api.namespace(
    name='Users',
    description='Endpoints del modulo Users',
    path='/users'
)

request_schema = UserRequestSchema(user_ns)


@user_ns.route('')
@user_ns.doc(security='Bearer')
class UsersListCreate(Resource):
    @jwt_required()
    @user_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todos los usuarios '''
        query_params = request_schema.all().parse_args()
        controller = UserController()
        return controller.fetch_all(query_params)

    @jwt_required()
    @user_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creacion de un usuario '''
        controller = UserController()
        return controller.save(request.json)


@user_ns.route('/<int:id>')
@user_ns.doc(security='Bearer')
class UsersGetUpdateDelete(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un usuario por su id '''
        controller = UserController()
        return controller.find_by_id(id)

    @jwt_required()
    @user_ns.expect(request_schema.update(), validate=True)
    def patch(self, id):
        ''' Actualizar un usuario por su id '''
        controller = UserController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Eliminar un usuario por su id '''
        controller = UserController()
        return controller.remove(id)
