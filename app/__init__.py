from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

from app.config import environment


app = Flask(__name__)
app.config.from_object(environment)

api = Api(
    app,
    title='Boilerplate Flask',
    version='0.1',
    description='RESTApi del Boilerplate',
    doc='/swagger-ui'
)

db = SQLAlchemy(app)
