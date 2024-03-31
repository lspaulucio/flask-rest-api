from mongoengine import Document, StringField, EmailField, DateTimeField
from flask_restx import fields, Model

model = Model(
    "UserModel",
    {
        "cpf": fields.String,
        "name": fields.String,
        "mail": fields.String,
        "birthDate": fields.Date,
    },
)


class UserModel(Document):
    cpf = StringField(required=True, unique=True)
    name = StringField(required=True)
    mail = EmailField(required=True, unique=True)
    birthDate = DateTimeField(required=True)
