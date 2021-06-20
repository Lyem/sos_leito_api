from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from features.on.on import On
from features.register_hospital.register_hospital import RegisterHospital
from features.register_user.register_user import RegisterUser

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

api.add_resource(On, '/')
api.add_resource(RegisterHospital, '/register/hospital')
api.add_resource(RegisterUser, '/register/user')

if __name__ == '__main__':
    app.run()