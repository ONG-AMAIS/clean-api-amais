from flask_restful import Api
from amais.presentation.controllers.user.create_patient_controller import CreatePatientController
from amais.presentation.controllers.user.create_collaborator_controller import CreateColaboratorController
from amais.presentation.controllers.user.create_voluntary_controller import CreateVoluntaryController
from amais.presentation.controllers.user.list_all_users_controller import ListAllUsersController
from amais.presentation.controllers.user.update_user_controller import UpdateUserController
from amais.presentation.controllers.user.delete_user_controller import DeleteUserController
from amais.presentation.controllers.user.user_login_controller import UserLoginController
from amais.presentation.controllers.donation.create_donation_controller import CreateDonationController
from amais.presentation.controllers.donation.list_all_donations_controller import ListAllDonationsController
from amais.presentation.controllers.talk.create_talk_controller import CreateTalkController


def load_routes(api: Api):
    api.add_resource(CreateColaboratorController, '/users/contributors')
    api.add_resource(CreateVoluntaryController, '/users/volunteers')
    api.add_resource(CreatePatientController, '/users/patients')
    api.add_resource(ListAllUsersController, '/users')
    api.add_resource(UpdateUserController, '/users/<int:user_id>')
    api.add_resource(DeleteUserController, '/users/<int:user_id>')
    api.add_resource(UserLoginController, '/login')

    api.add_resource(CreateDonationController, '/donations')
    api.add_resource(ListAllDonationsController, '/donations')

    api.add_resource(CreateTalkController, '/talks')
