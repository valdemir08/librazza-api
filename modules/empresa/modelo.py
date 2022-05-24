class Empresa:
    VALIDATE_FIELDS_REQUIREMENTS = ['nome', 'cnpj']

    def __init__(self, nome, cnpj, id=None):
        self.nome = nome
        self.cnpj = cnpj
        self.id = id

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return 'Nome: {} - CNPJ: {} '.format(self.nome, self.cnpj)

    def get_values_save(self):
        return [self.nome, self.cnpj]

    def get_json_formatter(self):
        data = {
            'id': self.id,
            'nome': self.nome,
            'cnpj': self.cnpj,
        }
        return data
