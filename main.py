from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from features.on.on import On
from features.register_hospital.register_hospital import RegisterHospital
from features.register_user.register_user import RegisterUser

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={
	r"/*":{
		"origins": "http://127.0.0.1:5500"
	}
})
api = Api(app)

api.add_resource(On, '/')
api.add_resource(RegisterHospital, '/register/hospital')
api.add_resource(RegisterUser, '/register/user')

if __name__ == '__main__':
    app.run()