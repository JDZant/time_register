class BaseController:
    _db_connection = None

    @classmethod
    def set_db_connection(cls, connection):
        cls._db_connection = connection

    @classmethod
    def get_db_connection(cls):
        return cls._db_connection
