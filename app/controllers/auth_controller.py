from os import getenv
from app import db, mail
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_mail import Message
from app.utils.mailing import Mailing
from http import HTTPStatus
from secrets import token_hex


class AuthController:
    def __init__(self):
        self.db = db
        self.model = UserModel
        self.mailing = Mailing()

    def signin(self, body):
        try:
            username = body['username']
            # 1º Validar que el usuario exista y este activo
            record = self.model.where(username=username, status=True).first()
            if record:
                # 2º Validar que la contraseña sea el del usuario
                password = body['password']
                if record.check_password(password):
                    # 3º Creacion de access_token
                    user_id = record.id
                    access_token = create_access_token(identity=user_id)
                    refresh_token = create_refresh_token(identity=user_id)

                    return {
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }, HTTPStatus.OK

                return {
                    'message': 'Contraseña incorrecta'
                }, HTTPStatus.UNAUTHORIZED

            return {
                'message': f'No se encontro el usuario: {username}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def refresh_token(self, identity):
        try:
            access_token = create_access_token(identity=identity)
            return {
                'access_token': access_token
            }, HTTPStatus.OK
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def password_reset(self, body):
        try:
            email = body['email']
            record = self.model.where(email=email, status=True).first()
            if record:
                new_password = token_hex(6)
                record.password = new_password
                record.hash_password()

                self.db.session.add(record)
                self.db.session.commit()

                self.mailing.mail_reset_password(
                    f'{record.name} {record.last_name}', email, new_password
                )

                return {
                    'message': 'Se envio la contraseña nueva'
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro el usuario: {email}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
