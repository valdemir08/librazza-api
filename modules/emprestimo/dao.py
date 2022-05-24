
_SCRIPT_SQL_INSERT = 'INSERT INTO EMPRESTIMOS(cliente_id, funcionario_id, livro_id, data_inicio, prazo_devolucao, data_devolucao, status) values (%s, %s, %s, %s, %s, %s, %s) returning id'
_SCRIPT_SQL_SELECT = 'SELECT * FROM EMPRESTIMOS'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM EMPRESTIMOS where id={}'
_SCRIPT_SQL_UPDATE_BY_ID = 'UPDATE EMPRESTIMOS SET {} WHERE ID={}'
_SCRIPT_SQL_DELETE_BY_ID = 'DELETE FROM EMPRESTIMOS WHERE ID={}'

class EmprestimoDao:
    def __init__(self, database):
        self.database = database

    def save(self, emprestimo):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, emprestimo.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        emprestimo.set_id(id)
        return emprestimo


    def edit(self, id, data_emprestimo):
        cursor = self.database.connect.cursor()
        str = []
        for key in data_emprestimo.keys():
            str.append('{}=%s'.format(key))
        cursor.execute(_SCRIPT_SQL_UPDATE_BY_ID.format(','.join(str), id), list(data_emprestimo.values()))
        self.database.connect.commit()
        cursor.close()
        return True

    def get_by_id(self, id):
        emprestimos = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if emprestimos:
            return emprestimos[0]
        return None

    def get_all(self):
        emprestimos = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return emprestimos

    def _get_all_or_by_id(self, script):
        emprestimos = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        emprestimo_cursor = cursor.fetchone()
        while emprestimo_cursor:
            emprestimo = dict(zip(columns_name, emprestimo_cursor))
            emprestimo_cursor = cursor.fetchone()
            emprestimos.append(emprestimo)
        cursor.close()
        return emprestimos

    def delete_by_id(self, id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_DELETE_BY_ID.format(id))
        self.database.connect.commit()
        cursor.close()