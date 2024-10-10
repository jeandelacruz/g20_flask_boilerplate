from app import api
from flask import request
from flask_restx import Resource
from app.controllers.roles_controller import RoleController
from app.schemas.roles_schema import RoleRequestSchema

role_ns = api.namespace(
    name='Roles',
    description='Endpoints del modulo Roles',
    path='/roles'
)

schema_request = RoleRequestSchema(role_ns)


# CRUD
'''
1. Traer todos los registros - /roles | GET
2. Crear un registro - /roles | POST
'''


@role_ns.route('')
class RolesListCreate(Resource):
    # dispatch
    def get(self):
        ''' Listar todos los roles '''
        controller = RoleController()
        return controller.fetch_all()

    @role_ns.expect(schema_request.create(), validate=True)
    def post(self):
        ''' Creacion de un rol '''
        controller = RoleController()
        return controller.save(request.json)


'''
3. Obtener un registro por el ID - /roles/path_params | GET
4. Actualizar un registro por el ID - /roles/path_params | PUT / PATCH
5. Eliminar un registro por el ID - /roles/path_params | DELETE
'''


@role_ns.route('/<int:id>')
class RolesGetUpdateDelete(Resource):
    def get(self, id):
        ''' Obtener un rol por su id '''
        controller = RoleController()
        return controller.find_by_id(id)

    @role_ns.expect(schema_request.update(), validate=True)
    def patch(self, id):
        ''' Actualizar un rol por su id '''
        controller = RoleController()
        return controller.update(id, request.json)

    def delete(self, id):
        ''' Eliminar un rol por su id '''
        controller = RoleController()
        return controller.remove(id)
