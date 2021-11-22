from flask_restful import Resource
from amais.presentation.helpers.http_helper import not_found, ok
from flask_restful import Resource, reqparse
from amais.data.usecases.user.update_user import UpdateUser


class UpdateUserController(Resource):
    @classmethod
    def put(self, user_id: int):

        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str)
        parser.add_argument('password',  type=str)

        args = parser.parse_args()

        success = UpdateUser().update(
            user_id, login=args['login'], password=args['password'])

        if not success:
            return not_found('Usuário não encontrado.', payload={})

        return ok(message='Usuário atualizado com sucesso!', payload={})
