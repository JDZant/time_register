import os

from dotenv import load_dotenv
from ..model.user import User
from ..services.ExternalAuthService import ExternalAuthService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


class AuthenticationController:
    def __init__(self, driver, db_connection):
        self.db_connection = db_connection
        self.external_auth_service = ExternalAuthService()
        self.driver = driver

    def login_user(self, email, password):
        # This method is for logging into the application itself.
        try:
            user = User(self.db_connection, email)
            if user.check_password(password):
                # User authenticated, proceed to application
                return True
            else:
                # Authentication failed
                return False
        except Exception as e:
            # Handle exception, such as a user not found
            return False

    def register_user(self, email, password):
        try:
            # Check if the user already exists
            existing_user = User.find_by_email(self.db_connection, email)
            if existing_user:
                return False, "User already exists."

            # Create a new user instance
            new_user = User(email, password, self.db_connection)
            # Hash the password
            new_user.set_password(password)
            # Save the new user to the database
            new_user.save()
            return True, "User registered successfully."
        except Exception as e:
            # Log the exception or handle it as needed
            return False, f"An error occurred: {e}"

    def login(self, username, password):
        base_url = os.getenv('TIME_REG_URL')

        # Navigate to the time registration page
        self.driver.get(f'{base_url}/2024-01-18')

        # Wait for the login field to be present before attempting to interact with it
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "_username")))

        # Now find the login field and enter the username
        username_field = self.driver.find_element(By.ID, "_username")
        username_field.send_keys(username)

        # Repeat for the password field
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "_password")))
        password_field = self.driver.find_element(By.ID, "_password")
        password_field.send_keys(password)

        # Wait for the submit button to be clickable and then click it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        submit_button = self.driver.find_element(By.ID, "login-button")
        submit_button.click()
