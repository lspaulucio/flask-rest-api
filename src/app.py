from flask import Flask
from flask_restx import Resource, Api
from flask_mongoengine import MongoEngine

from controllers.userController import UsersResource, UserResource

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flaskAPI',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'
}

api = Api(app)
db = MongoEngine(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<string:cpf>')
api.add_resource(UserResource, '/user')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
