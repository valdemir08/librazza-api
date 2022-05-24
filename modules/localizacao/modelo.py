
class Localizacao:
    def __init__(self, estante, prateleira, id=None):
        self.estante = estante
        self.prateleira = prateleira
        self.id = id

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return 'Nome: {} - CPF: {}'.format(self.estante, self.prateleira)

    def get_values_save(self, livro_id):
        return [self.estante, self.prateleira, livro_id]



