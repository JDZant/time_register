# main_view.py
from datetime import datetime
import tkinter as tk
from tkcalendar import DateEntry
from app.controller.authentication_controller import AuthenticationController
from app.controller.time_registration_controller import TimeRegistrationController
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from ..services.ExternalAuthService import ExternalAuthService


class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Time Registration")

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
        # self.date_input = tk.Entry(self, textvariable=self.date)
        self.start_time_input = tk.Entry(self, textvariable=self.start_time)
        self.preparation_duration_input = tk.Entry(self, textvariable=self.preparation_duration)
        self.standup_duration_input = tk.Entry(self, textvariable=self.standup_duration)
        self.time_registration_duration_input = tk.Entry(self, textvariable=self.time_registration_duration)

        # Buttons
        self.start_button = tk.Button(self, text="Start", command=self.start_process)

        # Positioning
        self.layout_widgets()

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
        self.start_button.grid(row=current_row, column=0, columnspan=2, padx=padx, pady=pady, sticky='ew')

    def start_process(self):
        user_config = {
            'date': self.date_input.get(),
            'start_time': self.start_time.get(),
            'preparation_duration': self.preparation_duration.get(),
            'standup_duration': self.standup_duration.get(),
            'time_registration_duration': self.time_registration_duration.get(),
        }

        # Instantiate the controllers
        service = Service('/usr/bin/chromedriver')
        driver = webdriver.Chrome(service=service)
        username = os.getenv('TIME_REG_USER')
        password = os.getenv('TIME_REG_PASS')

        login = ExternalAuthService()
        login.login(username, password, user_config['date'])

        TimeRegistrationController(driver, user_config)

        # Close the browser once done
        driver.quit()
