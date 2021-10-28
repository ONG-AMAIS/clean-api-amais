from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

teste = [{'id':1, 'titulo':'teste titulo 1'}]

@api.route('/teste')
class Test(Resource):
    def get(self, ):
        return teste, 200

    def post(self, ):
        payload = api.payload
        teste.append(payload)
        return payload, 201