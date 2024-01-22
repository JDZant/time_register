# main.py (or wherever your main function resides)
import os
import tkinter as tk
from dotenv import load_dotenv

from app.controller.general_view_controller import GeneralViewController
from app.controller.main_controller import MainController
from app.database.database_connection_manager import DatabaseConnectionManager
from app.database.database_connection import DatabaseConnection
from app.model.base.base_model import BaseModel
from app.controller.navigation_controller import NavigationController

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
        root.geometry('600x300')

        # Database init
        BaseModel.set_db_connection(db_connection)
        DatabaseConnectionManager.set_db_connection(db_connection)

        # ViewController init
        MainController(root)
        navigation_controller = NavigationController(root)

        # Show login view
        navigation_controller.show_login_view()

        root.mainloop()
    else:
        print("Failed to connect to the database")


if __name__ == "__main__":
    main()
