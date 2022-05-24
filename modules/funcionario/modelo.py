
class Funcionario:
    def __init__(self,matricula, senha, nome, cpf, telefone, email, data_nascimento, empresa_id, id=None):
        self.matricula = matricula
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        self.empresa_id = empresa_id
        self.id = id

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return 'Matrícula: {} - Senha: {} - Nome: {} - CPF: {} - Telefone: {} - Email: {} - Data de Nascimento: {} - Empresa id: {} '.format(self.matricula, self.senha, self.nome, self.cpf, self.telefone, self.email, self.data_nascimento, self.empresa_id)

    def get_values_save(self):
        return [self.matricula, self.senha, self.nome, self.cpf, self.telefone, self.email, self.data_nascimento, self.empresa_id]
