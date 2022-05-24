
_SCRIPT_SQL_INSERT = 'INSERT INTO AUTORES_LIVROS(autor_id, livro_id) values (%s, %s) returning id'
_SCRIPT_SQL_SELECT = 'SELECT * FROM AUTORES_LIVROS'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM AUTORES_LIVROS where id={}'
_SCRIPT_SQL_UPDATE_BY_ID = 'UPDATE AUTORES_LIVROS SET {} WHERE ID={}'

class AutoresLivrosDao:
    def __init__(self, database):
        self.database = database

    def save(self, autor_livro):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, autor_livro.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        autor_livro.set_id(id)
        return autor_livro


    def edit(self, id, data_autor_livro):
        cursor = self.database.connect.cursor()
        str = []
        for key in data_autor_livro.keys():
            str.append('{}=%s'.format(key))
        cursor.execute(_SCRIPT_SQL_UPDATE_BY_ID.format(','.join(str), id), list(data_autor_livro.values()))
        self.database.connect.commit()
        cursor.close()
        return True

    def get_by_id(self, id):
        autores_livros = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if autores_livros:
            return autores_livros[0]
        return None

    def get_all(self):
        autores_livros = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return autores_livros

    def _get_all_or_by_id(self, script):
        autores_livros = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        autor_livro_cursor = cursor.fetchone()
        while autor_livro_cursor:
            autor_livro = dict(zip(columns_name, autor_livro_cursor))
            autor_livro_cursor = cursor.fetchone()
            autores_livros.append(autor_livro)
        cursor.close()
        return autores_livros