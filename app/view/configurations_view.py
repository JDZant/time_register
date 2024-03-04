# configurations_view.py
import tkinter as tk
from tkinter import ttk
from ..controller.time_registration_config_controller import \
    TimeRegistrationConfigController  # Adjust import as necessary


class ConfigurationsView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.tree = None
        self.master = master

        # Setup Treeview
        self.setup_configurations_table()

        # Load configurations into the table
        self.load_configurations()

    def setup_configurations_table(self):
        self.tree = ttk.Treeview(self)

        # Define columns
        self.tree['columns'] = ('ID', 'Name', 'Start Date', 'Start Time', 'Preparation Duration', 'Standup Duration',
                                'Time Registration Duration')

        # Format columns
        self.tree.column("#0", width=0, stretch=tk.NO)  # Phantom column
        self.tree.column("ID", anchor=tk.W, width=80)
        self.tree.column("Name", anchor=tk.W, width=120)
        self.tree.column("Start Date", anchor=tk.W, width=100)
        self.tree.column("Start Time", anchor=tk.W, width=80)
        self.tree.column("Preparation Duration", anchor=tk.W, width=150)
        self.tree.column("Standup Duration", anchor=tk.W, width=130)
        self.tree.column("Time Registration Duration", anchor=tk.W, width=200)

        # Create Headings
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("ID", text="ID", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Start Date", text="Start Date", anchor=tk.W)
        self.tree.heading("Start Time", text="Start Time", anchor=tk.W)
        self.tree.heading("Preparation Duration", text="Preparation Duration", anchor=tk.W)
        self.tree.heading("Standup Duration", text="Standup Duration", anchor=tk.W)
        self.tree.heading("Time Registration Duration", text="Time Registration Duration", anchor=tk.W)

        # Pack the treeview finally
        self.tree.pack(expand=True, fill='both')

    def load_configurations(self):
        # Fetch configurations using the controller
        configs = TimeRegistrationConfigController.get_all_time_registration_configs()

        # Insert items into the treeview
        for config in configs:
            print(config)
            self.tree.insert('', 'end', values=(config.id, config.name, config.start_date, config.start_time,
                                                config.preparation_duration, config.standup_duration,
                                                config.time_registration_duration))
