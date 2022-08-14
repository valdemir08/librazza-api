
class Cliente:
    def __init__(self, nome, cpf, telefone, email, data_nascimento, confiabilidade_id, empresa_id, id=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        self.id = id
        self.confiabilidade_id = confiabilidade_id
        self.empresa_id = empresa_id
        self.endereco = None

    def set_id(self, id):
        self.id = id

    def set_endereco(self, endereco):
        self.endereco = endereco

    def set_confiabilidade_id(self, confiabilidade_id):
        self.confiabilidade_id = confiabilidade_id

    def __str__(self):
        return 'Nome: {} - CPF: {} - Telefone: {} - Email: {} - Data de Nascimento: {} - Confiabilidade id: {} - Empresa id: {}'.format(self.nome, self.cpf, self.telefone, self.email, self.data_nascimento, self.confiabilidade_id, self.empresa_id)

    def get_values_save(self):
        return [self.nome, self.cpf, self.telefone, self.email, self.data_nascimento, self.confiabilidade_id, self.empresa_id]




