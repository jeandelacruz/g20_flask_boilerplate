from app import api
from flask_restx import Resource
from app.controllers.roles_controller import RoleController

role_ns = api.namespace(
    name='Roles',
    description='Endpoints del modulo Roles',
    path='/roles'
)


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
        return controller.all()

    def post(self):
        ''' Creacion de un rol '''
        return 'Creación de rol'


'''
3. Obtener un registro por el ID - /roles/path_params | GET
4. Actualizar un registro por el ID - /roles/path_params | PUT / PATCH
5. Eliminar un registro por el ID - /roles/path_params | DELETE
'''
