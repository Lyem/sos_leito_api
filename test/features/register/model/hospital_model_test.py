import sys
sys.path.insert(1, 'C:/Users/Rafael/Documents/Github/sos_leito_api')
from features.register.model.hospital_model import HospitalModel
import json
import unittest

json_string = """ {
    "nome": "Hospital Dr. José Luiz de Gusmão",
    "endereco":{
        "logradouro": "Rua Marechal Rondon",
        "numero": "1600",
        "cep": "13308-458",
        "cidade": "Sorocaba",
        "bairro": "Vila Nova",
        "estado": "SP"
    },
    "telefone": "(11) 1528-9801",
    "publico?": true,
    "cnes": "1234567890"
} """

data = json.loads(json_string)

class MyTest(unittest.TestCase):
    def test(self):
        model = HospitalModel(data)
        datajson = model.toJson()
        self.assertEqual(model.endereco.cidade, 'Sorocaba')
        self.assertEqual(datajson['endereco']['cidade'], 'Sorocaba')

if __name__ == '__main__':
    unittest.main()