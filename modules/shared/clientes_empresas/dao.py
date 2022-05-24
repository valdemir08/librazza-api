
_SCRIPT_SQL_INSERT = 'INSERT INTO CLIENTES_EMPRESAS(cliente_id, empresa_id) values (%s, %s) returning id'
_SCRIPT_SQL_SELECT = 'SELECT * FROM CLIENTES_EMPRESAS'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM CLIENTES_EMPRESAS where id={}'
_SCRIPT_SQL_UPDATE_BY_ID = 'UPDATE CLIENTES_EMPRESAS SET {} WHERE ID={}'

class ClientesEmpresasDao:
    def __init__(self, database):
        self.database = database

    def save(self, cliente_empresa):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, cliente_empresa.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        cliente_empresa.set_id(id)
        return cliente_empresa


    def edit(self, id, data_cliente_empresa):
        cursor = self.database.connect.cursor()
        str = []
        for key in data_cliente_empresa.keys():
            str.append('{}=%s'.format(key))
        cursor.execute(_SCRIPT_SQL_UPDATE_BY_ID.format(','.join(str), id), list(data_cliente_empresa.values()))
        self.database.connect.commit()
        cursor.close()
        return True

    def get_by_id(self, id):
        clientes_empresas = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if clientes_empresas:
            return clientes_empresas[0]
        return None

    def get_all(self):
        clientes_empresas = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return clientes_empresas

    def _get_all_or_by_id(self, script):
        clientes_empresas = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        cliente_empresa_cursor = cursor.fetchone()
        while cliente_empresa_cursor:
            cliente_empresa = dict(zip(columns_name, cliente_empresa_cursor))
            cliente_empresa_cursor = cursor.fetchone()
            clientes_empresas.append(cliente_empresa)
        cursor.close()
        return clientes_empresas