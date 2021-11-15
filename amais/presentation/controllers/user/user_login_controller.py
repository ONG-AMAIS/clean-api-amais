from flask_restful import Resource
from amais.presentation.helpers.http_helper import notFound, ok, unauthorized
from flask_restful import Resource, reqparse
from amais.data.usecases.user.user_login import UserLogin


class UserLoginController(Resource):
    @classmethod
    def post(cls):

        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str)
        parser.add_argument('password',  type=str)

        args = parser.parse_args()

        success = UserLogin().login(
            login=args['login'], password=args['password'])

        if not success:
            return unauthorized('Usuário ou senha não encontrada.', payload={})

        return ok(message='Autenticação realizada com sucesso!', payload={})
