from flask_restful import Resource
from amais.presentation.helpers.http_helper import notFound, ok, unauthorized
from flask_restful import Resource, reqparse
from amais.data.usecases.user.user_login import UserLogin
from amais.utils.exceptions import Error


class UserLoginController(Resource):
    @classmethod
    def post(cls):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('login', type=str)
            parser.add_argument('password',  type=str)

            args = parser.parse_args()

            user = UserLogin().login(**args)
            return ok(message='Autenticação realizada com sucesso!', payload=user)
        except Error as error:
            CASES = {'INCORRECT_CREDENTIALS': unauthorized(
                'Usuário ou senha não encontrada.', payload={})}
            return CASES[error.title]
