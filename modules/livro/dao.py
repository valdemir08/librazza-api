
_SCRIPT_SQL_INSERT = 'INSERT INTO LIVROS(titulo, edicao, editora, ano_publicacao, num_paginas, cod_barras, genero, disponivel, empresa_id, isbn) values (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s) returning id'
_SCRIPT_SQL_SELECT = 'SELECT * FROM LIVROS'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM LIVROS where id={}'
_SCRIPT_SQL_UPDATE_BY_ID = 'UPDATE LIVROS SET {} WHERE ID={}'
_SCRIPT_SQL_SELECT_BY_ISBN = 'SELECT * FROM LIVROS where isbn={}'
_SCRIPT_SQL_DELETE_BY_ID = 'DELETE FROM LIVROS WHERE ID={}'

class LivroDao:
    def __init__(self, database):
        self.database = database

    def save(self, livro):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, livro.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        livro.set_id(id)
        return livro


    def edit(self, id, data_livro):
        cursor = self.database.connect.cursor()
        str = []
        for key in data_livro.keys():
            str.append('{}=%s'.format(key))
        cursor.execute(_SCRIPT_SQL_UPDATE_BY_ID.format(','.join(str), id), list(data_livro.values()))
        self.database.connect.commit()
        cursor.close()
        return True


    def get_by_isbn(self, isbn):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_SELECT_BY_ISBN.format(isbn))
        columns_name = [column[0] for column in cursor.description]
        livro_cursor = cursor.fetchone()
        livro = dict(zip(columns_name, livro_cursor))
        return livro


    def get_by_id(self, id):
        livros = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if livros:
            return livros[0]
        return None

    def get_all(self):
        livros = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return livros

    def _get_all_or_by_id(self, script):
        livros = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        livro_cursor = cursor.fetchone()
        while livro_cursor:
            livro = dict(zip(columns_name, livro_cursor))
            livro_cursor = cursor.fetchone()
            livros.append(livro)
        cursor.close()
        return livros

    def delete_by_id(self, id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_DELETE_BY_ID.format(id))
        self.database.connect.commit()
        cursor.close()