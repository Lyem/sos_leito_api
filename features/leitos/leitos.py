from flask import request
from flask_restful import Resource
from shared.db import Db
import bcrypt

class Leitos(Resource):
    def get(self):
        data = request.json
        db = Db()
        leitos = db.findAll('leitos',data)
        l = []
        for x in leitos:
            json = {"nome": x['nome'], "qtdtotal": x['qtdTotal'], "total": x['qtd'], "cnes": x['cnes']}
            l.append[json]
        return {'leitos': l}