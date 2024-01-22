class BaseModel:
    def __init__(self):
        self.db_connection = self.get_db_connection()
        self.cursor = self.db_connection.cursor()
        _db_connection = None

    @classmethod
    def set_db_connection(cls, connection):
        cls._db_connection = connection

    @classmethod
    def get_db_connection(cls):
        return cls._db_connection

    @classmethod
    def store(cls):
        # Implement saving logic in subclasses
        raise NotImplementedError

    @classmethod
    def delete(cls):
        # Implement deletion logic in subclasses
        raise NotImplementedError
