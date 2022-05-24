import psycopg2

class ConnectDB:
    _instance = None
    def __init__(self):

        self._connect = psycopg2.connect(
            host="localhost",
            database="librazza_db",
            user="postgres",
            password="postgres"
        )

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property#isenta do uso de parenteses quando for chamado
    def connect(self):
        return self._connect
