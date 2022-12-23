from flask_restx import Api
from flask import Blueprint, Flask, Response
from .database import init_db
from .controllers.usersController import api as users_ns
from prometheus_client.core import CollectorRegistry
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST


def create_app(config):
    app = Flask(__name__)
    blueprint = Blueprint('api', __name__)
    app.register_blueprint(blueprint)
    app.config.from_object(config)

    registry = CollectorRegistry()
    metrics = PrometheusMetrics.for_app_factory(registry=registry)

    api = Api(app, title='Flask REST API',
              version='1.0',
              description='Simple REST API built in python using flask framework',
              prefix='/api/v1',
              doc='/api-docs')

    init_db(app)

    api.add_namespace(users_ns, path='/users')

    metrics.init_app(app)

    @app.route('/metrics')
    def metrics():
        data = generate_latest(registry)
        return Response(data, mimetype=CONTENT_TYPE_LATEST)

    return app
