class BaseModel:
    def __init__(self, db_connection):
        self.conn = db_connection
        self.cursor = self.conn.cursor(dictionary=True)

    def save(self):
        # Implement saving logic in subclasses
        raise NotImplementedError

    def delete(self):
        # Implement deletion logic in subclasses
        raise NotImplementedError
