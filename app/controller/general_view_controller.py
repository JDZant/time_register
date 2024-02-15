from tkinter import simpledialog

from app.controller.main_controller import MainController
from app.model.time_registration_config import TimeRegistrationConfig


class GeneralViewController(MainController):
    def __init__(self, root):
        super().__init__(root)
        self.time_registration_config = TimeRegistrationConfig


    def show_save_as(self, data):
        name = simpledialog.askstring("Save Configuration", "Enter a name to save this configuration:")
        if name:
            time_reg_config = TimeRegistrationConfig(name=name,
                                                     start_date=data['date'],
                                                     start_time=data['start_time'],
                                                     preparation_duration=data['preparation_duration'],
                                                     standup_duration=data['standup_duration'],
                                                     time_registration_duration=data['time_registration_duration'])
            time_reg_config.store()
