import bcrypt

from app.model.base.base_model import BaseModel


class User(BaseModel):
    def __init__(self):
        super().__init__()
        self.id = None
        self.password = None
        self.email = None

    def delete(self):
        query = "DELETE FROM users WHERE id = %s"
        val = (self.id,)
        self.cursor.execute(query, val)
        self.db_connection.commit()
        self.cursor.close()

    def set_password(self, new_password):
        hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed.decode('utf-8')

    def set_email(self, email):
        self.email = email

    def store(self):
        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        val = (self.email, self.password)
        try:
            with self.db_connection.cursor() as cursor:
                cursor.execute(query, val)
                self.db_connection.commit()
                self.id = cursor.lastrowid
        except Exception as e:
            print(f"An error occurred: {e}")

