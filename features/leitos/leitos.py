from flask import request
from flask_restful import Resource
from shared.db import Db

class Leitos(Resource):
    def get(self):
        data = request.json
        db = Db()
        leitos = db.findAll('leitos',data)
        l = []
        for x in leitos:
            l.append(x)
        return {'leitos': l}