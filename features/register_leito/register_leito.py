from features.register_leito.model.leito_model import leitoModel
from flask import request
from flask_restful import Resource
from shared.db import Db

class RegisterLeito(Resource):
    def post(self):
        data = request.json
        model = leitoModel(data)
        db = Db()
        db.insert('leitos',{'nome': model.nome,'qtd': model.qtd, 'cnes': model.cnes})
        return {'status': 'ok'}