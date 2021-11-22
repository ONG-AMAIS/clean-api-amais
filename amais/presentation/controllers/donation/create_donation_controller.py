from flask_restful import Resource
from amais.presentation.helpers.http_helper import created
from flask_restful import Resource, reqparse
from amais.data.usecases.donation.create_donation import CreateDonation


class CreateDonationController(Resource):
    @ classmethod
    def post(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('donor', type=str)
        parser.add_argument('description',  type=str)
        parser.add_argument('value',  type=str)

        args = parser.parse_args()

        CreateDonation().create(
            description=args['description'], value=args['value'], donor=args['donor'])

        return created(message='Cadastro efetuado com sucesso!', payload={})
