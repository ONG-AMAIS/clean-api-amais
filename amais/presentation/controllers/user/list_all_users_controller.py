from flask_restful import Resource
from amais.presentation.helpers.http_helper import ok
from amais.data.usecases.list_all_users import ListAllUsers


class ListAllUsersController(Resource):

    @classmethod
    def get(self):
        users = ListAllUsers().list()
        return ok(message='Listagem efetuada com sucesso!', payload=users)
