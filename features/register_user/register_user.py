from flask import request
from flask_restful import Resource
from shared.db import Db
import bcrypt

class RegisterUser(Resource):
    def post(self):
        data = request.json
        db = Db()
        hospital = db.find('hospital', {'cnes': data['cnes']})
        json = {'email': data['email'],'senha': bcrypt.hashpw(data['senha'].encode('utf-8'),bcrypt.gensalt())
, 'permissao': data['permissao'],'id_hospital': hospital['_id']}
        db.insert('usuario', json)
        return {'status': 'ok'}