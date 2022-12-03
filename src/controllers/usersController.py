from flask import jsonify
from flask_restx import Namespace, Resource, reqparse
from werkzeug.exceptions import BadRequest

from mongoengine import NotUniqueError

from models.userModel import model, UserModel
from utils.helpers import cpf_validator

api = Namespace('Users', description='Users management')

api.models[model.name] = model

user_parser = reqparse.RequestParser()

user_parser.add_argument('cpf',
                         type=str,
                         required=True,
                         help='This field cannot be blank!')

user_parser.add_argument('name',
                         type=str,
                         required=True,
                         help='This field cannot be blank!')

user_parser.add_argument('mail',
                         type=str,
                         required=True,
                         help='This field cannot be blank!')

user_parser.add_argument('birthDate',
                         type=str,
                         required=True,
                         help='This field cannot be blank!')


@api.route('/')
class UsersController(Resource):
    @api.response(200, 'Success')
    def get(self):
        return jsonify(UserModel.objects())

    @api.doc(responses={204: 'Success', 400: 'Bad Request'})
    @api.expect(model)
    def post(self):
        payload = user_parser.parse_args()

        if not cpf_validator(payload.get('cpf')):
            raise BadRequest('Invalid CPF! Please enter with a valid one')

        try:
            user = UserModel(**payload).save()
        except NotUniqueError:
            return BadRequest('CPF already exists in database!')

        return '', 204


@api.route('/<cpf>')
class UserIdController(Resource):
    @api.response(200, 'Success')
    @api.response(404, 'Not found')
    def get(self, cpf: int):
        response = UserModel.objects(cpf=cpf)

        if response:
            return jsonify(response)
        else:
            return {'message': 'User not found in database!'}, 404
