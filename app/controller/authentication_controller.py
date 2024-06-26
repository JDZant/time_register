from dotenv import load_dotenv

from app.database.database_connection_manager import DatabaseConnectionManager
from ..model.user import User
from ..services.external_auth_service import ExternalAuthService

load_dotenv()


class AuthenticationController(DatabaseConnectionManager):
    def __init__(self):
        self.external_auth_service = ExternalAuthService()

    def login_user(self, email, password):
        try:
            user = User()
            if user.auth(email, password):
                return True
        except Exception as e:
            return False

    def register_user(self, email, password):
        try:
            new_user = User()
            new_user.set_password(password)
            new_user.set_email(email)
            new_user.store()

            return True, "User registered successfully."
        except Exception as e:
            return False, f"An error occurred: {e}"
