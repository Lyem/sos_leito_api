from flask import request
from flask_restful import Resource
from shared.db import Db

class GetUsers(Resource):
    def get(self):
        data = request.json
        db = Db()
        leitos = db.findAll('usuario',{"cnes": data['cnes']})
        l = []
        for x in leitos:
            l.append({"nome": x['email'],"permissao":x['permissao'],"cnes": x['cnes']})
        return {'users': l}