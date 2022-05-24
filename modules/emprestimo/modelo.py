
class Emprestimo:
    def __init__(self, data_inicio, prazo_devolucao, data_devolucao, status, cliente_id, funcionario_id, livro_id, id=None):
        self.data_inicio = data_inicio
        self.prazo_devolucao = prazo_devolucao
        self.data_devolucao = data_devolucao
        self.status = status
        self.cliente_id = cliente_id
        self.funcionario_id = funcionario_id
        self.livro_id = livro_id
        self.id = id

    def set_id(self, id):
        self.id = id
    def set_data_inicio(self, data_inicio):
        self.data_inicio = data_inicio

    def __str__(self):
        return 'Data início: {} - Prazo devolução: {} - Data devolução: {} - Status: {} - Cliente_id: {} - Funcionário_id: {} - Livro_id: {}'.format(self.data_inicio, self.prazo_devolucao, self.data_devolucao, self.status, self.cliente_id, self.funcionario_id, self.livro_id)

    def get_values_save(self):
        return [self.cliente_id, self.funcionario_id, self.livro_id, self.data_inicio, self.prazo_devolucao, self.data_devolucao, self.status]
