from features.login.model.user_model import user
from flask import request
from flask_restful import Resource
from shared.db import Db

class Login(Resource):
    def post(self):
        data = request.json
        model = user(data)
        retorno = Db.find('usuario',{'email': model.user})
        print(retorno)
        