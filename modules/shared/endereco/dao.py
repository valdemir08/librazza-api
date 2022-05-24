_SCRIPT_SQL_INSERT = 'INSERT INTO ENDERECOS (tipo_logradouro, logradouro, numero, bairro, cidade, cep, estado, cliente_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) returning id'
_SCRIPT_SQL_SELECT_ALL = 'SELECT * FROM ENDERECOS'
_SCRIPT_SQL_SELECT_BY_CLIENTE_ID = 'SELECT * FROM ENDERECOS where cliente_id={}'


class EnderecoDao:
    def __init__(self, database):
        self.database = database

    def save(self, endereco, cliente_id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, endereco.get_values_save(cliente_id))
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        endereco.set_id(id)
        return endereco


    def get_endereco_by_cliente_id(self, id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_SELECT_BY_CLIENTE_ID.format(id))
        columns_name = [column[0] for column in cursor.description]
        endereco = cursor.fetchone()
        if endereco:
            endereco = dict(zip(columns_name, endereco))
        cursor.close()
        return endereco
