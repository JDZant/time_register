from tkinter import ttk, simpledialog

from ..view.configurations_view import ConfigurationsView
from ..view.general_view import GeneralView


class NavigationController:
    def __init__(self, root):
        self.configurations_view = None
        self.root = root
        self.current_view = None
        self.notebook = None
        self.general_tab = None
        self.configurations_tab = None

    def create_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Create frames for each tab
        self.general_tab = ttk.Frame(self.notebook)
        self.configurations_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.general_tab, text='General')
        self.notebook.add(self.configurations_tab, text='Configurations')

    # Navigation
    def show_login_view(self):
        self.clear_current_view()
        self.current_view = LoginView(master=self.root, on_login_success=self.setup_main_menu)
        self.current_view.pack()

    def show_general_view(self):
        self.clear_current_view()
        self.current_view = GeneralView(master=self.general_tab)
        self.current_view.pack()

    def clear_current_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
            self.current_view = None

    def show_configurations_view(self):
        # Clear the configurations tab before adding new content
        for widget in self.configurations_tab.winfo_children():
            widget.destroy()

        # Create and pack the ConfigurationsView
        self.configurations_view = ConfigurationsView(master=self.configurations_tab)
        self.configurations_view.pack(expand=True, fill='both')

    def setup_main_menu(self):
        self.clear_current_view()
        self.create_notebook()
        self.show_general_view()
        self.show_configurations_view()

