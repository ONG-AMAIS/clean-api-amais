from .helper.http_helper import created, ok
from flask_restful import Resource, reqparse
from amais.data.usecase.create_user import CreateUser
from amais.data.usecase.list_all_users import ListAllUsers


class UserResource(Resource):
    @classmethod
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str)
        parser.add_argument('password',  type=str)

        args = parser.parse_args()

        CreateUser().create(login=args.login, password=args.password)

        return created(message='Listagem efetuada com sucesso!', payload={})

    @classmethod
    def get(self):
        users = ListAllUsers().list()
        return ok(message='Listagem efetuada com sucesso!', payload=users)
