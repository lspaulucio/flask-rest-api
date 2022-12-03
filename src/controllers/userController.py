from flask_restx import Resource, reqparse
from flask import jsonify

from utils.helpers import cpf_validator


from models.userModel import UserModel
from werkzeug.exceptions import BadRequest, InternalServerError
import logging


class UsersResource(Resource):
    def get(self):
        return {'message': "Hi"}


class UserResource(Resource):
    __user_parser = reqparse.RequestParser()

    __user_parser.add_argument('cpf',
                               type=str,
                               required=True,
                               help="This field cannot be blank!")

    __user_parser.add_argument('name',
                               type=str,
                               required=True,
                               help="This field cannot be blank!")

    __user_parser.add_argument('mail',
                               type=str,
                               required=True,
                               help="This field cannot be blank!")

    __user_parser.add_argument('birthDate',
                               type=str,
                               required=True,
                               help="This field cannot be blank!")

    def get(self, cpf):
        return {'message': "Hi cpf"}

    def post(self):
        payload = self.__user_parser.parse_args()

        if not cpf_validator(payload.get('cpf')):
            raise BadRequest("Invalid CPF!")

        user = UserModel(**payload).save()

        return {'a': '%s' % user.id}, 201
