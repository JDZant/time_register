from dotenv import load_dotenv

from app.controller.base.base_controller import BaseController
from ..model.user import User
from ..services.ExternalAuthService import ExternalAuthService

load_dotenv()


class AuthenticationController(BaseController):
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
            # Check if the user already exists
            existing_user = User.find_by_email(email)
            if existing_user:
                return False, "User already exists."

            new_user = User()
            new_user.set_password(password)
            new_user.set_email(email)
            new_user.save()

            return True, "User registered successfully."
        except Exception as e:
            return False, f"An error occurred: {e}"
