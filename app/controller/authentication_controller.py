import os

from datetime import datetime, timedelta
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


class Login:
    def __init__(self, driver, date):
        self.driver = driver
        self.date = date

    def login(self, username, password):
        base_url = os.getenv('TIME_REG_URL')

        # Navigate to the time registration page
        self.driver.get(f'{base_url}/{self.date}')

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
