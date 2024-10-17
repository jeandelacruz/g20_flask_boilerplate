from app import api
from flask import request
from flask_restx import Resource
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
