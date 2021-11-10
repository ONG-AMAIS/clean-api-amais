from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from src.resource.person_resource import PersonsResource, PersonResource

APP = Flask(__name__)
API = Api(APP)
CORS(APP)

API.add_resource(PersonsResource, '/persons')
API.add_resource(PersonResource, '/person/<int:person_id>')

if __name__ == '__main__':
    APP.run(debug=True)