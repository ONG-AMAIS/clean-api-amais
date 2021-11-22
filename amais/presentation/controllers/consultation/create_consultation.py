from flask_restful import Resource
from amais.presentation.helpers.http_helper import created, not_found, bad_request
from flask_restful import Resource, reqparse
from amais.data.usecases.talk.create_talk import CreateTalk
from werkzeug.datastructures import FileStorage
from amais.utils.exceptions import Error


class CreateTalkController(Resource):
    @ classmethod
    def post(cls):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('patient_document', type=str)
            parser.add_argument('date',  type=str)
            parser.add_argument('address',  type=str)
            parser.add_argument('guidelines',  type=str)
            parser.add_argument('volunteer_document',  type=str)
            parser.add_argument('address',  type=str)
            parser.add_argument('annex', type=FileStorage, location='files')

            args = parser.parse_args()

            file = args['annex']

            CreateTalk().create(file=file, title=args['title'], address=args['address'],
                                date=args['date'], description=args['description'],
                                duration=args['duration'], price=args['price'],
                                presenter_document=args['presenter_document'])

            return created(message='Cadastro efetuado com sucesso!', payload={})

        except Error as error:
            CASES = {
                'PERSON_NOT_FOUND': not_found(message='Cliente não encontrado.', payload={}),
                'EXTENSION_NOT_ALLOWED': bad_request(message='Extensão não permitida, envie um template html.', payload={})
            }

            return CASES[error.title]
