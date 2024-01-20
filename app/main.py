# main.py (or wherever your main function resides)
import os
import tkinter as tk
from dotenv import load_dotenv

from app.controller.base.base_controller import BaseController
from app.database.database_connection import DatabaseConnection
from app.model.base.base_model import BaseModel
from app.controller.authentication_controller import AuthenticationController
from app.view.login_view import LoginView

# Load environment variables
load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
}


def main():
    db_connection = DatabaseConnection.get_instance(db_config)
    if db_connection:
        root = tk.Tk()
        root.title(os.getenv('APPLICATION_NAME'))
        root.geometry("400x200")

        BaseModel.set_db_connection(db_connection)
        BaseController.set_db_connection(db_connection)

        auth_controller = AuthenticationController()
        login_view = LoginView(auth_controller, master=root)

        login_view.pack()
        root.mainloop()
    else:
        print("Failed to connect to the database")


if __name__ == "__main__":
    main()
