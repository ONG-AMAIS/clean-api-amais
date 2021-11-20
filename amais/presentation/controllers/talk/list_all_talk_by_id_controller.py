from flask_restful import Resource
from amais.presentation.helpers.http_helper import ok, notFound
from amais.utils.exceptions import Error
from amais.data.usecases.talk.list_all_talk_by_id import ListTalkByid


class ListTalkByIdController(Resource):

    @classmethod
    def get(self, talk_id: int):
        try:
            talk = ListTalkByid().list(talk_id)
            return ok(message='Listagem efetuada com sucesso!', payload=talk)

        except Error as error:
            CASES = {'NOT_FOUND':
                     notFound(message='Não foi possível encontrar a palestra solicitada.', payload={})}

            return CASES[error.title]
