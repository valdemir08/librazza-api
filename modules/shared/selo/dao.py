_SCRIPT_SQL_INSERT = 'INSERT INTO SELOS (valor_selo) VALUES (%s) returning id'
_SCRIPT_SQL_SELECT_ALL = 'SELECT * FROM SELOS'
_SCRIPT_SQL_SELECT_BY_ID = 'SELECT * FROM SELOS where id={}'


class SeloDao:
    def __init__(self, database):
        self.database = database

    def save(self, selo):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_INSERT, selo.get_values_save())
        id = cursor.fetchone()[0]
        self.database.connect.commit()
        cursor.close()
        selo.set_id(id)
        return selo


    def get_selo_by_id(self, id):
        cursor = self.database.connect.cursor()
        cursor.execute(_SCRIPT_SQL_SELECT_BY_ID.format(id))
        columns_name = [column[0] for column in cursor.description]
        selo = cursor.fetchone()
        if selo:
            selo = dict(zip(columns_name, selo))
        cursor.close()
        return selo
