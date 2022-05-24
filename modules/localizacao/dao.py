
_SCRIPT_SQL_INSERT = 'INSERT INTO LOCALIZACOES(estante, prateleira, livro_id) values (%s, %s, %s) returning id'
_SCRIPT_SQL_SELECT = 'SELECT * FROM LOCALIZACOES'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM LOCALIZACOES where id={}'
_SCRIPT_SQL_UPDATE_BY_ID = 'UPDATE LOCALIZACOES SET {} WHERE ID={}'

class LocalizacaoDao:
    def __init__(self, database):
        self.database = database

    def save(self, localizacao, livro_id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, localizacao.get_values_save(livro_id))
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        localizacao.set_id(id)
        return localizacao


    def edit(self, id, data_localizacao):
        cursor = self.database.connect.cursor()
        str = []
        for key in data_localizacao.keys():
            str.append('{}=%s'.format(key))
        cursor.execute(_SCRIPT_SQL_UPDATE_BY_ID.format(','.join(str), id), list(data_localizacao.values()))
        self.database.connect.commit()
        cursor.close()
        return True

    def get_by_id(self, id):
        localizacoes = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if localizacoes:
            return localizacoes[0]
        return None

    def get_all(self):
        localizacoes = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return localizacoes

    def _get_all_or_by_id(self, script):
        localizacoes = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        localizacao_cursor = cursor.fetchone()
        while localizacao_cursor:
            localizacao = dict(zip(columns_name, localizacao_cursor))
            localizacao_cursor = cursor.fetchone()
            localizacoes.append(localizacao)
        cursor.close()
        return localizacoes