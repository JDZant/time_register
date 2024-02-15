from tkinter import simpledialog

from app.controller.main_controller import MainController
from app.model.time_registration_config import TimeRegistrationConfig


class GeneralViewController(MainController):
    def __init__(self, root):
        super().__init__(root)
        self.time_registration_config = TimeRegistrationConfig


    def show_save_as(self):
        name = simpledialog.askstring("Save Configuration", "Enter a name to save this configuration:")
        if name:
            time_reg_config = TimeRegistrationConfig(name=name, start_date="2024-01-01", start_time="09:00:00",
                                            preparation_duration=15, standup_duration=15, time_registration_duration=30)
            time_reg_config.store()
