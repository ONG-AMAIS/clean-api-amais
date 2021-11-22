from flask_restful import Resource
from amais.presentation.helpers.http_helper import ok
from flask_restful import Resource
from amais.data.usecases.donation.list_all_donations import ListAllDonations


class ListAllDonationsController(Resource):
    @ classmethod
    def get(cls):

        donations = ListAllDonations().list()
        return ok(message='Doações listadas com sucesso!', payload=donations)
