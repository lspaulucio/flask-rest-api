from flask_restx import Api
from flask import Blueprint, Flask
from .database import init_db
from .controllers.usersController import api as users_ns


def create_app(config):
    app = Flask(__name__)
    blueprint = Blueprint('api', __name__)
    app.register_blueprint(blueprint)
    app.config.from_object(config)

    api = Api(app, title='Flask REST API',
              version='1.0',
              description='Simple REST API built in python using flask framework',
              prefix='/api/v1',
              doc='/api-docs')

    init_db(app)

    api.add_namespace(users_ns, path='/users')

    return app
