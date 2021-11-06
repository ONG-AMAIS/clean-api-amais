import traceback
from flask_restful import Resource, reqparse

from src.repository.person_repository import PersonRepository

teste = [{'id':1, 'titulo':'teste titulo 1'}]

class PersonResource(Resource):
    def get(self):
        return teste, 200
    
    @classmethod
    def post(self):
        attributes = reqparse.RequestParser()
        attributes.add_argument(
            'name',
            type=str,
            required=True,
            help="O campo 'name' é obrigatorio."
        )
        attributes.add_argument(
            'cpf',
            type=str,
            required=True,
            help="O campo 'cpf' é obrigatorio."
        )
        attributes.add_argument(
            'phone',
            type=str,
            required=True,
            help="O campo 'phone' é obrigatorio."
        )
        attributes.add_argument('email', type=str, required=False)                                                                
        attributes.add_argument('rg', type=str, required=False)
        attributes.add_argument('active', type=bool)

        data = attributes.parse_args()

        person_repository = PersonRepository()

        try:
            # PersonRepository = user.save_user()
            person_result = person_repository.insert(**data)
            return {'message': 'Pessoa criada na base', 'data': person_result}, 201
        except Exception as ex:
            traceback.print_exc()
            return {'message': f'An internal server error has occured: {ex}.'}, 500

 