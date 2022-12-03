from flask import Blueprint, Flask
from flask_restx import Resource, Api
from flask_mongoengine import MongoEngine

from controllers.usersController import api as users_ns


app = Flask(__name__)
blueprint = Blueprint('api', __name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flaskAPI',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'
}

api = Api(app, title='Flask REST API', version='1.0',
          description='Simple REST API built in python using flask framework', prefix='/api/v1')
db = MongoEngine(app)

api.add_namespace(users_ns, path='/users')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
