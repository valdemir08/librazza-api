
_SCRIPT_SQL_INSERT = 'INSERT INTO FUNCIONARIOS(matricula, senha, nome, cpf, telefone, email, data_nascimento, empresa_id) values (%s, %s, %s, %s, %s, %s, %s, %s) returning id'
_SCRIPT_SQL_SELECT = 'select * from FUNCIONARIOS'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM FUNCIONARIOS where id={}'
_SCRIPT_SQL_UPDATE_BY_ID = 'UPDATE FUNCIONARIOS SET {} WHERE ID={}'
_SCRIPT_SQL_DELETE_BY_ID = 'DELETE FROM FUNCIONARIOS WHERE ID={}'

class FuncionarioDao:
    def __init__(self, database):
        self.database = database

    def save(self, funcionario):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, funcionario.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        funcionario.set_id(id)
        return funcionario


    def edit(self, id, data_funcionario):
        cursor = self.database.connect.cursor()
        str = []
        for key in data_funcionario.keys():
            str.append('{}=%s'.format(key))
        cursor.execute(_SCRIPT_SQL_UPDATE_BY_ID.format(','.join(str), id), list(data_funcionario.values()))
        self.database.connect.commit()
        cursor.close()
        return True

    def get_by_id(self, id):
        funcionarios = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if funcionarios:
            return funcionarios[0]
        return None

    def get_all(self):
        funcionarios = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return funcionarios

    def _get_all_or_by_id(self, script):
        funcionarios = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        funcionario_cursor = cursor.fetchone()
        while funcionario_cursor:
            funcionario = dict(zip(columns_name, funcionario_cursor))
            funcionario_cursor = cursor.fetchone()
            funcionarios.append(funcionario)
        cursor.close()
        return funcionarios

    def delete_by_id(self, id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_DELETE_BY_ID.format(id))
        self.database.connect.commit()
        cursor.close()