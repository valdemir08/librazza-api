
class AutoresLivros:
    def __init__(self, autor_id, livro_id, id=None):
        self.autor_id = autor_id
        self.livro_id = livro_id
        self.id = id

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return 'Autor id: {} - Livro id: {}'.format(self.autor_id, self.livro_id)

    def get_values_save(self):
        return [self.autor_id, self.livro_id]



