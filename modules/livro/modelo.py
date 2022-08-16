
class Livro:
    def __init__(self, titulo, edicao, editora, ano_publicacao, num_paginas, cod_barras, genero, disponivel, empresa_id, isbn, id=None, localizacao_id=None):
        self.titulo = titulo
        self.edicao = edicao
        self.editora = editora
        self.ano_publicacao = ano_publicacao
        self.num_paginas = num_paginas
        self.cod_barras = cod_barras
        self.genero = genero
        self.disponivel = disponivel
        self.isbn = isbn
        self.id = id
        self.empresa_id = empresa_id
        self.localizacao_id = localizacao_id
        self.autor = None

    def set_id(self, id):
        self.id = id
    
    def set_localizacao_id(self, localizacao_id):
        self.localizacao_id = localizacao_id

    def set_autor_id(self, id):
        self.autor_id = id


    def __str__(self):
        return 'Título: {} - Edição: {} - Editora: {} - Ano Publicação: {} - Cod Barras: {} - Gênero: {} - Disponível: {}  - ISBN: {}'.format(self.titulo, self.edicao, self.editora, self.ano_publicacao, self.num_paginas, self.cod_barras, self.genero, self.disponivel, self.isbn)

    def get_values_save(self):
        return [self.titulo, self.edicao, self.editora, self.ano_publicacao, self.num_paginas, self.cod_barras, self.genero, self.disponivel, self.empresa_id, self.isbn, self.localizacao_id]



