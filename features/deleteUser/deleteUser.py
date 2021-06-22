from flask import request
from flask_restful import Resource
from shared.db import Db

class DeleteUser(Resource):
    def post(self):
        data = request.json
        db = Db()
        db.delete('usuario',data)
        return {'status': 'ok'}