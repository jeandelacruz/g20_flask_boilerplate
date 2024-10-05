from app.models.roles_model import RoleModel


class RoleController:
    def __init__(self):
        self.model = RoleModel

    def all(self):
        return 'Listado de roles'
