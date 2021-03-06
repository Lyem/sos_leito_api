from features.login.model.user_model import user
from flask import request
from flask_restful import Resource
from shared.db import Db
import bcrypt

class Login(Resource):
    def post(self):
        data = request.json
        model = user(data)
        db = Db()
        data = {'email': model.user}
        retorno = db.find('usuario',data)
        if(bcrypt.hashpw(model.senha.encode('utf-8'), retorno['senha'])==retorno['senha']):
            permissao = retorno['permissao']
            cnes = retorno['cnes']
            return {'status': True, 'email': model.user, 'permissao': permissao, 'cnes': cnes}
        else:
            return {'status': False}