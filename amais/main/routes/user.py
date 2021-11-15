from .helper.http_helper import created, ok
from flask_restful import Resource, reqparse
from amais.infra.db.user.user_repository import UserRepository


class UserResource(Resource):
    @classmethod
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str)
        parser.add_argument('password',  type=str)

        args = parser.parse_args()

        user_repository = UserRepository()

        user_repository.insert(
            login=args['login'], password=args['password'])

        return created(message='Listagem efetuada com sucesso!', payload={})

    @classmethod
    def get(self):
        user_repository = UserRepository()
        users = user_repository.get_all()
        return ok(message='Listagem efetuada com sucesso!', payload=users)
