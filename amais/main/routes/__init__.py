from flask_restful import Api
from amais.presentation.controllers.user.create_user_controller import CreateUserController
from amais.presentation.controllers.user.list_all_users_controller import ListAllUsersController
from amais.presentation.controllers.user.update_user_controller import UpdateUserController
from amais.presentation.controllers.user.delete_user_controller import DeleteUserController


def load_routes(api: Api):
    api.add_resource(CreateUserController, '/users')
    api.add_resource(ListAllUsersController, '/users')
    api.add_resource(UpdateUserController, '/users/<int:user_id>')
    api.add_resource(DeleteUserController, '/users/<int:user_id>')
