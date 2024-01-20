# external_auth_service.py in the services directory
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ExternalAuthService:
    def __init__(self):
        self.driver = None
        pass

    def initialize_driver(self):
        # Initialize the Selenium WebDriver only if it hasn't been initialized already
        if self.driver is None:
            service = Service('/usr/bin/chromedriver')
            self.driver = webdriver.Chrome(service=service)

    @staticmethod
    def authenticate(username, password):
        # Use Selenium to log in to the external time registration website.
        # This is just a placeholder for the actual logic.
        driver = webdriver.Chrome()  # Or however you configure your driver
        # ... perform actions to log in ...
        success = True  # Change based on actual success or failure
        return success

    def login(self, username, password):
        self.initialize_driver()
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
