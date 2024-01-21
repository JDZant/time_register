import mysql.connector


class DatabaseConnection:
    _instance = None

    @classmethod
    def get_instance(cls, config):
        if cls._instance is None:
            cls._instance = cls.create_db_connection(config)
        return cls._instance

    @staticmethod
    def create_db_connection(config):
        try:
            connection = mysql.connector.connect(**config)
            if connection.is_connected():
                return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
