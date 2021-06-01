import json

class HospitalModel:
    def __init__(self, json):
        self.nome = json['nome']
        self.endereco = Endereco(json['endereco'])
        self.telefone = json['telefone']
        self.publico = json['publico?']
        self.cnes = json['cnes']
    
    def toJson(self):
        json_string = '{"nome": "'+ self.nome + '", "endereco":{ "logradouro": "'+ self.endereco.logradouro + '", "numero": "'+ self.endereco.numero + '", "cep": "'+ self.endereco.cep + '", "cidade": "'+ self.endereco.cidade + '", "bairro": "'+ self.endereco.bairro + '", "estado": "'+ self.endereco.estado + '"}, "telefone": "'+ self.telefone + '", "publico?": '+ str(self.publico).lower() + ', "cnes": "'+ self.cnes + '"}'
        data = json.loads(json_string)
        return data

class Endereco:
    def __init__(self, endereco):
        self.logradouro = endereco['logradouro']
        self.numero = endereco['numero']
        self.cep = endereco['cep']
        self.cidade = endereco['cidade']
        self.bairro = endereco['bairro']
        self.estado = endereco['estado']