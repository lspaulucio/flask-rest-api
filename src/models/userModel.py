from mongoengine import Document, StringField, EmailField, DateTimeField


class UserModel(Document):
    cpf = StringField(required=True, unique=True)
    name = StringField(required=True)
    mail = EmailField(required=True, unique=True)
    birthDate = DateTimeField(required=True)
