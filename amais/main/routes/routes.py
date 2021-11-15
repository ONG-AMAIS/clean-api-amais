from flask_restful import Api
from .user import UserResource


def load_routes(api: Api):
    api.add_resource(UserResource, '/users')
