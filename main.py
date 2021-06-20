from flask import Flask
from flask_restful import Api
from features.on.on import On
from flask_cors import CORS, cross_origin
from features.register_hospital.register_hospital import RegisterHospital
from features.register_user.register_user import RegisterUser

app = Flask(__name__)
api = Api(app)
cors = CORS(api, resources={r"/*": {"origins": "*"}})

api.add_resource(On, '/')
api.add_resource(RegisterHospital, '/register/hospital')
api.add_resource(RegisterUser, '/register/user')

if __name__ == '__main__':
    app.run()