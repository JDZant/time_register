import os
import mysql.connector
import tkinter as tk
from app.controller.authentication_controller import AuthenticationController
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from app.view.login_view import LoginView

# Load environment variables
load_dotenv()
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
}


def create_db_connection(config):
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def main():
    db_connection = create_db_connection(db_config)
    if db_connection:
        root = tk.Tk()  # Create the main Tkinter window
        auth_controller = AuthenticationController(db_connection=db_connection, driver=driver)

        # Create an instance of LoginView with the required arguments
        login_view = LoginView(auth_controller, master=root)

        login_view.pack()  # Pack the login_view into the root window
        root.mainloop()  # Start the Tkinter event loop
    else:
        print("Failed to connect to the database")
        if db_connection and db_connection.is_connected():
            db_connection.close()


if __name__ == "__main__":
    main()
