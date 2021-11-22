from flask_restful import Resource
from amais.presentation.helpers.http_helper import ok, not_found
from amais.utils.exceptions import Error
from amais.data.usecases.talk.list_all_talks import ListAllTalks


class ListAllTalksController(Resource):

    @classmethod
    def get(self):
        try:
            talks = ListAllTalks().list()
            return ok(message='Listagem efetuada com sucesso!', payload=talks)

        except Error as error:
            CASES = {'NOT_FOUND':
                     not_found(message='Não foi possível encontrar nenhuma palestra.', payload={})}
            return CASES[error.title]
