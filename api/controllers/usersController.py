from flask import jsonify
from flask_restx import Namespace, Resource, reqparse
from werkzeug.exceptions import BadRequest

from mongoengine import NotUniqueError

from ..models.userModel import model, UserModel
from ..utils.helpers import cpf_validator

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
    @api.response(204, 'Success')
    def get(self):
        return jsonify(UserModel.objects())

    @api.doc(responses={204: 'Success', 400: 'Bad Request'})
    @api.expect(model)
    def post(self):
        payload = user_parser.parse_args()

        if not cpf_validator(payload.get('cpf')):
            raise BadRequest('Invalid CPF! Please enter with a valid one!')

        try:
            UserModel(**payload).save()
        except NotUniqueError:
            raise BadRequest('CPF already exists in database!')

        return '', 204

    @api.expect(model)
    @api.response(200, 'Success')
    @api.response(304, 'Not modified')
    @api.response(400, 'Bad request')
    def patch(self):
        payload = user_parser.parse_args()
        cpf = payload.get('cpf')

        if not cpf_validator(cpf):
            raise BadRequest('Invalid CPF! Please enter with a valid one!')

        response = UserModel.objects(cpf=cpf)
        if response:
            try:
                response = UserModel.objects(cpf=cpf).update(**payload)
                return {"message": "User successfully updated!"}, 200
            except Exception:
                return {"message": "Error updating user!"}, 304
        else:
            return {'message': 'User not found in database!'}, 400


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

    @api.response(204, 'Success')
    @api.response(501, 'Error')
    @api.response(400, 'Bad request')
    def delete(self, cpf: int):
        response = UserModel.objects(cpf=cpf)
        if response:
            try:
                response = UserModel.objects(cpf=cpf).delete()
                return {"message": "User successfully deleted!"}, 200
            except Exception:
                return {"message": "Error deleting user!"}, 503
        else:
            return {"message": "User not found!"}, 400

    # @api.response(200, 'Busca realizada com sucesso')
    # @api.param('nome', 'Nome da pessoa')  # parametros customizados
    # @api.param('endereco', 'Endereço da pessoa')
    # def put(self, id: int):
    #     # return PessoaDb.alterar(int(id), request.json), 201
    #     return 200

    # @api.deprecated
    # def delete(self, id: int):
    #     # return PessoaDb.remover(int(id)), 200
    #     return 200

    # @api.hide
    # def patch(self):
    #     return 200
