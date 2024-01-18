# user.py in the model directory
import bcrypt

from .base_model import BaseModel


class User(BaseModel):
    def __init__(self, email, password, db_connection):
        super().__init__(db_connection)
        self.email = email
        self.set_password(password)
        self.id = None
        self.email = email
        self.password = password

    @classmethod
    def find_by_email(cls, db_connection, email):
        cursor = db_connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s"
        val = (email,)
        cursor.execute(query, val)
        result = cursor.fetchone()
        cursor.close()
        if result:
            user = cls(result['email'], result['password_hash'])
            user.id = result['id']
            return user
        return None

    def delete(self):
        query = "DELETE FROM users WHERE id = %s"
        val = (self.id,)
        self.cursor.execute(query, val)

    def set_password(self, new_password):
        # Hash the new password
        hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed.decode('utf-8')

    def check_password(self, password):
        # Check the password against the hashed version
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def save(self):
        # Ensure that self.password contains the hashed password before saving
        query = "INSERT INTO users (email, password_hash) VALUES (%s, %s)"
        val = (self.email, self.password)
        self.cursor.execute(query, val)
        self.id = self.cursor.lastrowid

