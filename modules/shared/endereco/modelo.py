class Endereco:
    VALIDATE_FIELDS_REQUIREMENTS = ['tipo_logradouro','logradouro', 'numero', 'bairro', 'cidade', 'cep', 'estado']

    def __init__(self, tipo_logradouro, logradouro, numero, bairro, cidade, cep, estado):
        self.id = None
        self.tipo_logradouro = tipo_logradouro
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.estado = estado


    def set_id(self, id):
        self.id = id

    def __str__(self):
        return 'Endereço: {} {} - Nº: {} Bairro: {} - Cidade: {} - {} CEP:{}'.format(self.tipo_logradouro ,self.logradouro, self.numero, self.bairro, self.cidade, self.estado, self.cep)

    def get_values_save(self, cliente_id):
        return [self.tipo_logradouro, self.logradouro, self.numero, self.bairro, self.cidade, self.cep, self.estado, cliente_id]
