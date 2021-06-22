from features.deleteLeito.delete_leito import DeleteLeitos
from features.leitos.leitos import Leitos
from features.register_leito.register_leito import RegisterLeito
from features.login.login import Login
from flask import Flask
from flask_restful import Api
from features.on.on import On
from features.register_hospital.register_hospital import RegisterHospital
from features.register_user.register_user import RegisterUser

app = Flask(__name__)
api = Api(app)

api.add_resource(On, '/')
api.add_resource(RegisterHospital, '/register/hospital')
api.add_resource(RegisterUser, '/register/user')
api.add_resource(Login, '/login')
api.add_resource(RegisterLeito, '/register/leito')
api.add_resource(Leitos, '/leitos')
api.add_resource(DeleteLeitos, '/delete/leitos')


if __name__ == '__main__':
    app.run()