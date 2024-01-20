import bcrypt

from app.model.base.base_model import BaseModel


class User(BaseModel):
    def __init__(self):
        super().__init__()
        self.id = None
        self.password = None
        self.email = None


    @classmethod
    def find_by_email(cls, email):
        db_connection = cls.get_db_connection()
        cursor = db_connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s"
        val = (email,)
        cursor.execute(query, val)
        result = cursor.fetchone()
        cursor.close()
        if result:
            user = cls(result['email'], result['password'])
            user.id = result['id']
            return user
        return None

    def delete(self):
        db_connection = self.get_db_connection()
        cursor = db_connection.cursor()
        query = "DELETE FROM users WHERE id = %s"
        val = (self.id,)
        cursor.execute(query, val)
        db_connection.commit()
        cursor.close()

    def set_password(self, new_password):
        hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed.decode('utf-8')

    def set_email(self, email):
        self.email = email

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def save(self):
        db_connection = self.get_db_connection()
        cursor = db_connection.cursor()
        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        val = (self.email, self.password)
        cursor.execute(query, val)
        db_connection.commit()
        self.id = cursor.lastrowid
        cursor.close()
