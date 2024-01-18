# main.py
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from app.controllers.authentication_controller import Login
from app.controllers.time_registration_controller import TimeRegistration

# Load environment variables
load_dotenv()


def run_time_registration(user_config):
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    username = os.getenv('TIME_REG_USER')
    password = os.getenv('TIME_REG_PASS')

    login = Login(driver, user_config['date'])

    # Login
    login.login(username, password)

    TimeRegistration(driver, user_config)

    # Close the browser once done
    driver.quit()
