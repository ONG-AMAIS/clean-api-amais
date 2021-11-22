from flask_restful import Resource
from amais.presentation.helpers.http_helper import created
from flask_restful import Resource, reqparse
from amais.data.usecases.user.create_voluntary import CreateVoluntary


class CreateVoluntaryController(Resource):
    @ classmethod
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str)
        parser.add_argument('password',  type=str)
        parser.add_argument('name',  type=str)
        parser.add_argument('cpf',  type=str)
        parser.add_argument('occupation',  type=str)
        parser.add_argument('occupation_description',  type=str)
        parser.add_argument('document_url',  type=str)
        parser.add_argument('rg',  type=str)
        parser.add_argument('phone',  type=str)
        parser.add_argument('email',  type=str)

        args = parser.parse_args()

        CreateVoluntary().create(**args)

        return created(message='Cadastro efetuado com sucesso!', payload={})
