from app import api
from flask_restx import Resource
from flask import Response
from http import HTTPStatus


health_ns = api.namespace(
    name='HealthCheck',
    description='Validación de recurso activo',
    path='/health'
)


@health_ns.route('')
class HealthCheck(Resource):
    def get(self):
        ''' Comprobar la salud del recurso '''
        return Response(status=HTTPStatus.OK)
