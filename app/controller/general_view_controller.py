from tkinter import simpledialog

from app.controller.main_controller import MainController


class GeneralViewController(MainController):
    def __init__(self, root):
        super().__init__(root)

    def show_save_as(self):
        name = simpledialog.askstring("Save Configuration", "Enter the name for this time registration configuration:")
