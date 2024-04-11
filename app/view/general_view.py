# general_view.py
from datetime import datetime
import tkinter as tk
from tkcalendar import DateEntry
from app.controller.time_registration_controller import TimeRegistrationController
import os

from ..controller.general_view_controller import GeneralViewController
from ..controller.main_controller import MainController
from ..controller.time_registration_config_controller import TimeRegistrationConfigController
from ..services.external_auth_service import ExternalAuthService


class GeneralView(tk.Frame, MainController):
    def __init__(self, master):
        super().__init__(master)
        self.time_reg_config = None
        self.master = master

        # Date
        self.date_input = DateEntry(self, date_pattern='y-mm-dd', year=datetime.now().year,
                                    month=datetime.now().month, day=datetime.now().day)

        # Start time
        self.start_time = tk.StringVar(None, '08:30')

        # Durations
        self.preparation_duration = tk.IntVar(None, 30)
        self.standup_duration = tk.IntVar(None, 30)
        self.time_registration_duration = tk.IntVar(None, 15)

        # Labels
        self.date_label = tk.Label(self, text="Enter date (Y-m-d)")
        self.start_time_label = tk.Label(self, text="Start time (H:M)")
        self.preparation_duration_label = tk.Label(self, text="Preparation duration (min)")
        self.standup_duration_label = tk.Label(self, text="Standup duration (min)")
        self.time_registration_duration_label = tk.Label(self, text="Time registration duration (min)")

        # Inputs
        self.start_time_input = tk.Entry(self, textvariable=self.start_time)
        self.preparation_duration_input = tk.Entry(self, textvariable=self.preparation_duration)
        self.standup_duration_input = tk.Entry(self, textvariable=self.standup_duration)
        self.time_registration_duration_input = tk.Entry(self, textvariable=self.time_registration_duration)

        # Buttons
        self.start_button = tk.Button(self, text="Start", command=self.start_process)
        self.save_as = tk.Button(self, text="Save as..", command=self.save_data)
        # Positioning
        self.layout_widgets()

        self.time_registration_config_controller = TimeRegistrationConfigController()
        self.set_time_registration_data()

    def layout_widgets(self):
        current_row = 1
        padx, pady = 10, 10

        # List of widget pairs (label, input) for easy iteration
        widget_pairs = [
            (self.date_label, self.date_input),
            (self.start_time_label, self.start_time_input),
            (self.preparation_duration_label, self.preparation_duration_input),
            (self.standup_duration_label, self.standup_duration_input),
            (self.time_registration_duration_label, self.time_registration_duration_input),
        ]

        # Iterate over the widget pairs and grid them
        for label, input in widget_pairs:
            label.grid(row=current_row, column=0, padx=padx, pady=pady, sticky='e')  # Align labels to the right
            input.grid(row=current_row, column=1, padx=padx, pady=pady, sticky='ew')  # Stretch input to fill the cell
            current_row += 1  # Increment the row counter for the next pair

        # Special case for the start button, which spans two columns
        self.start_button.grid(row=current_row, column=1, columnspan=1, padx=padx, pady=pady, sticky='ew')
        self.save_as.grid(row=current_row, column=3, columnspan=1, padx=padx, pady=pady, sticky='ew')

    def set_time_registration_data(self):
        config = self.time_registration_config_controller.get_time_registration_config_by_id(2)

        if config:
            start_date = datetime.strptime(config.start_date, '%Y-%m-%d')
            self.date_input.set_date(start_date)

            self.start_time.set(config.start_time)
            self.preparation_duration.set(config.preparation_duration)
            self.standup_duration.set(config.standup_duration)
            self.time_registration_duration.set(config.time_registration_duration)
        else:
            print("Configuration not found.")

    def get_time_registration_config_data(self):
        return {
            'date': self.date_input.get(),
            'start_time': self.start_time.get(),
            'preparation_duration': self.preparation_duration.get(),
            'standup_duration': self.standup_duration.get(),
            'time_registration_duration': self.time_registration_duration.get(),
        }

    def start_process(self):
        time_reg_config = self.get_time_registration_config_data()
        username = os.getenv('TIME_REG_USER')
        password = os.getenv('TIME_REG_PASS')
        auth_service = ExternalAuthService()
        auth_service.initialize_driver()
        auth_service.login(username, password, time_reg_config['date'])
        TimeRegistrationController(auth_service.get_chrome_driver(), time_reg_config)

    def save_data(self):
        # Update time_reg_config with the current values from the UI elements
        self.time_reg_config = {
            'date': self.date_input.get(),
            'start_time': self.start_time.get(),
            'preparation_duration': self.preparation_duration.get(),
            'standup_duration': self.standup_duration.get(),
            'time_registration_duration': self.time_registration_duration.get(),
        }
        # Call show_save_as with the updated time_reg_config
        GeneralViewController(self.get_root()).show_save_as(self.time_reg_config)
