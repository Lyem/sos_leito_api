from flask import request
from flask_restful import Resource
from shared.db import Db

class DeleteLeitos(Resource):
    def post(self):
        data = request.json
        db = Db()
        db.delete('leitos',data)
        return {'status': 'ok'}