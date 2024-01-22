from tkinter import ttk

from ..view.login_view import LoginView
from ..view.general_view import GeneralView
import tkinter as tk


class ViewController:
    def __init__(self, root):
        self.root = root
        self.current_view = None
        self.notebook = None
        self.general_tab = None
        self.settings_tab = None

    def create_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Create frames for each tab
        self.general_tab = ttk.Frame(self.notebook)
        self.settings_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.general_tab, text='General')
        self.notebook.add(self.settings_tab, text='Settings')

    # Navigation
    def show_login_view(self):
        self.clear_current_view()
        self.current_view = LoginView(master=self.root, on_login_success=self.setup_main_menu)
        self.current_view.pack()

    def show_main_view(self):
        self.clear_current_view()
        self.current_view = GeneralView(master=self.general_tab)
        self.current_view.pack()

    def clear_current_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
            self.current_view = None

    def setup_main_menu(self):
        self.clear_current_view()
        self.create_notebook()
        self.show_main_view()
