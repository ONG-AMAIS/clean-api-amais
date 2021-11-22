from flask_restful import Api
from flask_cors import CORS
from .application import app
from .routes import load_routes


api = Api(app)

CORS(app)

load_routes(api)
