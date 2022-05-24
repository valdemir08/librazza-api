

class Confiabilidade:
    def __init__(self, pontos, selo, qtd_livros_permitidos, qtd_livros_emprestados, id=None):
        self.pontos = pontos
        self.selo = selo
        self.qtd_livros_permitidos = qtd_livros_permitidos
        self.qtd_livros_emprestados = qtd_livros_emprestados
        self.id = id

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return 'Pontos: {} - Selo: {} - Qtd Livros Permitidos: {} - Qtd Livros Emprestados: {}'.format(self.pontos, self.selo,self.qtd_livros_permitidos, self.qtd_livros_emprestados)

    def get_values_save(self):
        return [self.pontos, self.selo, self.qtd_livros_permitidos, self.qtd_livros_emprestados]



