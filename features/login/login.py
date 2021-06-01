from flask import request
from flask_restful import Resource
from shared.db import Db

class Login(Resource):
    def post(self):
        data = request.json