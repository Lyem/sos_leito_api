from flask import request
from flask_restful import Resource
from shared.db import Db

class setQTD(Resource):
    def post(self):
        data = request.json
        db = Db()
        db.update('leitos',data['old'],data['new'])
        return {'status': 'ok'}