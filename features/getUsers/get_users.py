from flask import request
from flask_restful import Resource
from shared.db import Db

class GetUsers(Resource):
    def get(self):
        data = request.json
        db = Db()
        resposta = db.find('usuario',{"nome": data['nome']})
        leitos = db.findAll('usuario',resposta['id_hospital'])
        l = []
        for x in leitos:
            l.append(x)
        return {'users': l}