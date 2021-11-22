from flask_restful import Resource
from amais.presentation.helpers.http_helper import created
from flask_restful import Resource, reqparse
from amais.data.usecases.user.create_patient import CreatePatient


class CreatePatientController(Resource):
    @ classmethod
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str)
        parser.add_argument('password',  type=str)
        parser.add_argument('name',  type=str)
        parser.add_argument('cpf',  type=str)
        parser.add_argument('rg',  type=str)
        parser.add_argument('phone',  type=str)
        parser.add_argument('email',  type=str)
        parser.add_argument('address',  type=dict)
        parser.add_argument('deficiency',  type=str)
        parser.add_argument('do_therapy',  type=str)
        parser.add_argument('autism_level',  type=int)
        parser.add_argument('family_income',  type=str)
        parser.add_argument('special_ability',  type=str)

        args = parser.parse_args()

        CreatePatient().create(**args)

        return created(message='Cadastro efetuado com sucesso!', payload={})
