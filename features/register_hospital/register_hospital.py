from flask import request
from flask_restful import Resource
from flask_cors import CORS
from features.register_hospital.model.hospital_model import HospitalModel
from shared.db import Db

@cross_origin()
class RegisterHospital(Resource):
    def post(self):
        data = request.json
        hospital = HospitalModel(data)
        db = Db()
        db.insert('hospital', hospital.toJson())
        return {'status': 'ok'}