
_SCRIPT_SQL_INSERT = 'INSERT INTO AUTORES(nome) values (%s) returning id'
_SCRIPT_SQL_SELECT = 'SELECT * FROM AUTORES'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM AUTORES where id={}'
_SCRIPT_SQL_UPDATE_BY_ID = 'UPDATE AUTORES SET {} WHERE ID={}'
_SCRIPT_SQL_DELETE_BY_ID = 'DELETE FROM AUTORES WHERE ID={}'
_SCRIPT_SQL_SELECT_BY_AUTOR_NAME = 'SELECT * FROM AUTORES where nome={}'

class AutorDao:
    def __init__(self, database):
        self.database = database

    def save(self, autor):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, autor.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        autor.set_id(id)
        return autor


    def edit(self, id, data_autor):
        cursor = self.database.connect.cursor()
        str = []
        for key in data_autor.keys():
            str.append('{}=%s'.format(key))
        cursor.execute(_SCRIPT_SQL_UPDATE_BY_ID.format(','.join(str), id), list(data_autor.values()))
        self.database.connect.commit()
        cursor.close()
        return True

    def get_by_autor_name(self, autor_name):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_SELECT_BY_AUTOR_NAME.format(autor_name))
        columns_name = [column[0] for column in cursor.description]
        autor_cursor = cursor.fetchone()
        autor = dict(zip(columns_name, autor_cursor))
        return autor

    def get_by_id(self, id):
        autores = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if autores:
            return autores[0]
        return None

    def get_all(self):
        autores = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return autores

    def _get_all_or_by_id(self, script):
        autores = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        autor_cursor = cursor.fetchone()
        while autor_cursor:
            autor = dict(zip(columns_name, autor_cursor))
            autor_cursor = cursor.fetchone()
            autores.append(autor)
        cursor.close()
        return autores

    def delete_by_id(self, id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_DELETE_BY_ID.format(id))
        self.database.connect.commit()
        cursor.close()
