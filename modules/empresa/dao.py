
_SCRIPT_SQL_INSERT = 'INSERT INTO EMPRESAS(nome, cnpj) values (%s, %s) returning id'
_SCRIPT_SQL_SELECT = 'SELECT * FROM EMPRESAS'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM EMPRESAS where id={}'
_SCRIPT_SQL_UPDATE_BY_ID = 'UPDATE EMPRESAS SET {} WHERE ID={}'
_SCRIPT_SQL_SELECT_BY_CNPJ = 'SELECT * FROM EMPRESAS where cnpj={}'
_SCRIPT_SQL_DELETE_BY_ID = 'DELETE FROM EMPRESAS WHERE ID={}'

class EmpresaDao:
    def __init__(self, database):
        self.database = database

    def save(self, empresa):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, empresa.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        empresa.set_id(id)
        return empresa


    def edit(self, id, data_empresa):
        cursor = self.database.connect.cursor()
        str = []
        for key in data_empresa.keys():
            str.append('{}=%s'.format(key))
        cursor.execute(_SCRIPT_SQL_UPDATE_BY_ID.format(','.join(str), id), list(data_empresa.values()))
        self.database.connect.commit()
        cursor.close()
        return True


    def get_by_cnpj(self, cnpj):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_SELECT_BY_CNPJ.format(cnpj))
        columns_name = [column[0] for column in cursor.description]
        empresa_cursor = cursor.fetchone()
        empresa = dict(zip(columns_name, empresa_cursor))
        return empresa

    def get_by_id(self, id):
        empresas = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if empresas:
            return empresas[0]
        return None

    def get_all(self):
        empresas = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return empresas

    def _get_all_or_by_id(self, script):
        empresas = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        empresa_cursor = cursor.fetchone()
        while empresa_cursor:
            empresa = dict(zip(columns_name, empresa_cursor))
            empresa_cursor = cursor.fetchone()
            empresas.append(empresa)
        cursor.close()
        return empresas

    def delete_by_id(self, id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_DELETE_BY_ID.format(id))
        self.database.connect.commit()
        cursor.close()