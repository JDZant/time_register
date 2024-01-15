# main.py
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from app.login import Login
from app.time_registration import TimeRegistration

# Load environment variables
load_dotenv()


def run_time_registration(start_time):
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    username = os.getenv('TIME_REG_USER')
    password = os.getenv('TIME_REG_PASS')

    login = Login(driver)

    # Login
    login.login(username, password)

    TimeRegistration(driver, start_time)

    # Close the browser once done
    driver.quit()
