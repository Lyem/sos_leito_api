from flask import request
from flask_cors import CORS
from flask_restful import Resource
from shared.db import Db

@cross_origin()
class Login(Resource):
    def post(self):
        data = request.json