from app import db
from app.models.roles_model import RoleModel
from app.schemas.roles_schema import RoleResponseSchema
from http import HTTPStatus


class RoleController:
    def __init__(self):
        self.db = db
        self.model = RoleModel
        self.schema = RoleResponseSchema

    def fetch_all(self):
        records = self.model.where(status=True).all()
        roles = self.schema(many=True)
        return {
            'records': roles.dump(records)
        }, HTTPStatus.OK

    def save(self, body):
        try:
            record_new = self.model.create(name=body['name'])
            self.db.session.add(record_new)
            self.db.session.commit()
            return {
                'message': f'El rol {body["name"]} se creo con exito'
            }, HTTPStatus.CREATED
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def find_by_id(self, id):
        try:
            record = self.model.where(id=id, status=True).first()

            if record:
                role = self.schema(many=False)
                return {
                    'record': role.dump(record)
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro el ROL {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def update(self, id, body):
        try:
            record = self.model.where(id=id, status=True).first()

            if record:
                record.update(name=body['name'])
                self.db.session.add(record)
                self.db.session.commit()

                return {
                    'message': f'El Rol {id}, ha sido actualizado.'
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro el ROL {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def remove(self, id):
        try:
            record = self.model.where(id=id, status=True).first()

            if record:
                record.update(status=False)
                self.db.session.add(record)
                self.db.session.commit()

                return {
                    'message': f'El Rol {id}, ha sido removido.'
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro el ROL {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
