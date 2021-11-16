from flask_restful import Resource
from amais.presentation.helpers.http_helper import created
from flask_restful import Resource, reqparse
from amais.data.usecases.user.create_user import CreateUser


class CreateUserController(Resource):
    @ classmethod
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str)
        parser.add_argument('password',  type=str)
        parser.add_argument('name',  type=str)
        parser.add_argument('cpf',  type=str)
        parser.add_argument('type_id',  type=int)
        parser.add_argument('rg',  type=str)
        parser.add_argument('phone',  type=str)
        parser.add_argument('email',  type=str)

        args = parser.parse_args()

        CreateUser().create(**args)

        return created(message='Cadastro efetuado com sucesso!', payload={})
