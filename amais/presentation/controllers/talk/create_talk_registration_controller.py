from flask_restful import Resource
from amais.presentation.helpers.http_helper import created, not_found, unprocessable_entity
from flask_restful import Resource, reqparse
from amais.data.usecases.talk.create_talk_registration import CreateTalkRegistration
from werkzeug.datastructures import FileStorage
from amais.utils.exceptions import Error


class CreateTalkRegistrationController(Resource):
    @ classmethod
    def post(cls, talk_id: int):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str)
            parser.add_argument('cpf',  type=str)

            args = parser.parse_args()

            CreateTalkRegistration.create(**args, talk_id=talk_id)

            return created(message='Cadastro efetuado com sucesso!', payload={})

        except Error as error:
            CASES = {
                'TALK_NOT_FOUND': not_found(message='Palestra não encontrada.', payload={}),
                'REGISTER_ALREADY_EXISTS': unprocessable_entity('Já existe uma inscrição para esse cpf.', payload={})
            }

            return CASES[error.title]
