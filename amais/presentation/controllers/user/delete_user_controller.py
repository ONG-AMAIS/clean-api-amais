from flask_restful import Resource
from amais.presentation.helpers.http_helper import not_found, ok
from flask_restful import Resource
from amais.data.usecases.user.delete_user import DeleteUser


class DeleteUserController(Resource):
    @classmethod
    def delete(self, user_id: int):

        success = DeleteUser().delete(user_id)

        if not success:
            return not_found('Usuário não encontrado.', payload={})

        return ok(message='Usuário deletado com sucesso!', payload={})
