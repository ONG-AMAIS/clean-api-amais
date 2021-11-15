from flask_restful import Resource
from amais.presentation.helpers.http_helper import notFound, ok
from flask_restful import Resource
from amais.data.usecases.delete_user import DeleteUser


class DeleteUserController(Resource):
    @classmethod
    def delete(self, user_id: int):

        success = DeleteUser().delete(id=user_id)

        if not success:
            return notFound('Usuário não encontrado.', payload={})

        return ok(message='Usuário deletado com sucesso!', payload={})
