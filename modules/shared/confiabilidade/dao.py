

_SCRIPT_SQL_INSERT = 'INSERT INTO CONFIABILIDADES (pontos, qtd_livros_permitidos, qtd_livros_emprestados) VALUES (%s, %s, %s) returning id'
_SCRIPT_SQL_SELECT_ALL = 'SELECT * FROM CONFIABILIDADES'
_SCRIPT_SQL_SELECT_BY_CLIENTE_ID = 'SELECT * FROM CONFIABILIDADES where cliente_id={}'
_SCRIPT_SQL_SELECT = 'SELECT * FROM CONFIABILIDADES'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM CONFIABILIDADES where id={}'


class ConfiabilidadeDao:
    def __init__(self, database):
        self.database = database

    def save(self, confiabilidade):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, confiabilidade.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        confiabilidade.set_id(id)
        return confiabilidade

    def get_confiabilidade_by_cliente_id(self, id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_SELECT_BY_CLIENTE_ID.format(id))
        columns_name = [column[0] for column in cursor.description]
        confiabilidade = cursor.fetchone()
        if confiabilidade:
            confiabilidade = dict(zip(columns_name, confiabilidade))
        cursor.close()
        return confiabilidade

    def get_by_id(self, id):
        confiabilidades = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if confiabilidades:
            return confiabilidades[0]
        return None

    def get_all(self):
        confiabilidades = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return confiabilidades

    def _get_all_or_by_id(self, script):
        confiabilidades = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        confiabilidade_cursor = cursor.fetchone()
        while confiabilidade_cursor:
            confiabilidade = dict(zip(columns_name, confiabilidade_cursor))
            confiabilidade_cursor = cursor.fetchone()
            confiabilidades.append(confiabilidade)
        cursor.close()
        return confiabilidades
