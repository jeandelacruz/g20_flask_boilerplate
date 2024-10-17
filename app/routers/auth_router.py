from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.auth_controller import AuthController
from app.schemas.auth_schema import AuthRequestSchema

auth_ns = api.namespace(
    name='Authentication',
    description='Endpoints del modulo Autenticación',
    path='/auth'
)

request_schema = AuthRequestSchema(auth_ns)


@auth_ns.route('/signin')
class AuthLogin(Resource):
    @auth_ns.expect(request_schema.signin(), validate=True)
    def post(self):
        ''' Login de Usuario '''
        controller = AuthController()
        return controller.signin(request.json)


@auth_ns.route('/token/refresh')
class AuthRefreshToken(Resource):
    @jwt_required(refresh=True)
    @auth_ns.expect(request_schema.refresh_token(), validate=True)
    def post(self):
        ''' Obtener un nuevo access token desde el refresh token '''
        identity = get_jwt_identity()
        controller = AuthController()
        return controller.refresh_token(identity)


@auth_ns.route('/password/reset')
class AuthPasswordReset(Resource):
    @auth_ns.expect(request_schema.password_reset(), validate=True)
    def post(self):
        ''' Reinicio de contraseña del usuario '''
        controller = AuthController()
        return controller.password_reset(request.json)
