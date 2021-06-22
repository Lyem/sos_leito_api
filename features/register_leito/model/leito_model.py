class leitoModel:
    def __init__(self,json):
        self.nome = json['nome']
        self.qtd = json['qtd']
        self.cnes = json['cnes']