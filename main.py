import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from login import Login
from time_registration import TimeRegistration

load_dotenv()

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)
username = os.getenv('TIME_REG_USER')
password = os.getenv('TIME_REG_PASS')

login_page = Login(driver)
time_registration_page = TimeRegistration(driver)

# Login
login_page.login(username, password)

time.sleep(1)

# Register time
time_registration_page.register_time()

# Close the browser once done
driver.quit()
