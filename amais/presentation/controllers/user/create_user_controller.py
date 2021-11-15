from flask_restful import Resource
from amais.presentation.helpers.http_helper import created
from flask_restful import Resource, reqparse
from amais.data.usecases.create_user import CreateUser


class CreateUserController(Resource):
    @ classmethod
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str)
        parser.add_argument('password',  type=str)

        args = parser.parse_args()

        CreateUser().create(login=args.login, password=args.password)

        return created(message='Cadastro efetuado com sucesso!', payload={})
