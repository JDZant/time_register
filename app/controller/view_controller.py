import tkinter as tk
from ..view.login_view import LoginView


# import other views as needed

class ViewController:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def show_login_view(self):
        self.clear_current_view()
        self.current_view = LoginView(master=self.root, on_login_success=self.show_main_view)
        self.current_view.pack()

    def show_main_view(self):
        self.clear_current_view()
        from ..view.main_view import MainView
        self.current_view = MainView(master=self.root)
        self.current_view.pack()

    def clear_current_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
            self.current_view = None
