from modules.shared.endereco.dao import EnderecoDao

_SCRIPT_SQL_INSERT = 'INSERT INTO CLIENTES(nome, cpf, telefone, email, data_nascimento, confiabilidade_id) values (%s, %s, %s, %s, %s, %s) returning id'
_SCRIPT_SQL_SELECT = 'select * from clientes'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM CLIENTES where id={}'
_SCRIPT_SQL_UPDATE_BY_ID = 'UPDATE CLIENTES SET {} WHERE ID={}'
_SCRIPT_SQL_DELETE_BY_ID = 'DELETE FROM CLIENTES WHERE ID={}'

class ClienteDao:
    def __init__(self, database):
        self.database = database
        self.dao_endereco = EnderecoDao(database=database)

    def save(self, cliente):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, cliente.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        cliente.set_id(id)
        return cliente


    def edit(self, id, data_cliente):
        cursor = self.database.connect.cursor()
        str = []
        for key in data_cliente.keys():
            str.append('{}=%s'.format(key))
        cursor.execute(_SCRIPT_SQL_UPDATE_BY_ID.format(','.join(str), id), list(data_cliente.values()))
        self.database.connect.commit()
        cursor.close()
        return True

    def get_by_id(self, id):
        clientes = self._get_all_or_by_id(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        if clientes:
            return clientes[0]
        return None

    def get_all(self):
        clientes = self._get_all_or_by_id(_SCRIPT_SQL_SELECT)
        return clientes

    def _get_all_or_by_id(self, script):
        clientes = []
        cursor = self.database.connect.cursor()
        cursor.execute(script)
        columns_name = [column[0] for column in cursor.description]
        cliente_cursor = cursor.fetchone()
        while cliente_cursor:
            cliente = dict(zip(columns_name, cliente_cursor))
            cliente_cursor = cursor.fetchone()
            endereco = self.dao_endereco.get_endereco_by_cliente_id(cliente.get('id'))
            if endereco:
                endereco.pop('cliente_id')
            cliente['endereco'] = endereco
            clientes.append(cliente)
        cursor.close()
        return clientes

    def delete_by_id(self, id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_DELETE_BY_ID.format(id))
        self.database.connect.commit()
        cursor.close()