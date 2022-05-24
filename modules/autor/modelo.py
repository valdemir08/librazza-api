
class Autor:
    def __init__(self, nome,  id=None):
        self.nome = nome
        self.id = id

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return 'Nome: {}'.format(self.nome)

    def get_values_save(self):
        return [self.nome]
