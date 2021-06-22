from flask import request
from flask_restful import Resource
from shared.db import Db
import bcrypt

class Leitos(Resource):
    def get(self):
        data = request.json
        db = Db()
        leitos = db.findAll('leitos',data)
        print(leitos)
        return {'status': 'ok'}