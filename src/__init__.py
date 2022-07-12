from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config.from_object('src.config.DevelopmentConfig')


class hi(Resource):
    def get(self):
        return{
            'This is a test' : 'succes',
            'message' : 'Test was succesful'
        }

class Ping(Resource):
    def get(self):
        return{
            'status':'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')
api.add_resource(hi,'/hi')