from datetime import datetime, timedelta

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TimeRegistration:
    def __init__(self, driver, start_time):
        self.driver = driver
        self.preparation_info_end_time_string = None
        self.standup_info_end_time = None
        self.time_registration_info_end_time = None

        # Set default placeholder times
        self.preparation_info_placeholder = "08:30"

        # Set default time values
        self.preparation_info_time = 30
        self.standup_info_time = 30
        self.time_registration_info_time = 15

        # Set time registration arrays

        preparation_info = {
            "time_placeholder_identifier": self.preparation_info_placeholder,
            "time_value": start_time or '09:00',

            "select_id_1": 's2id_autogen1',
            "search_bar_id_1": 's2id_autogen2_search',
            "search_bar_value_1": '24005',

            "select_id_2": 's2id_autogen3',
            "search_bar_id_2": 's2id_autogen4_search',
            "search_bar_value_2": 'Overige werkzaamheden (specificeer)',

            "description": "Opstarten pc/laptop, klaarzetten werkomgeving, dag voorbereiden",
            "description_index": 0
        }

        standup_info = {
            "time_placeholder_identifier": None,
            "time_value": self.standup_info_end_time or '09:30',

            "select_id_1": 's2id_autogen5',
            "search_bar_id_1": 's2id_autogen6_search',
            "search_bar_value_1": '24005',

            "select_id_2": 's2id_autogen7',
            "search_bar_id_2": 's2id_autogen8_search',
            "search_bar_value_2": 'Vergaderen en stand-up',

            "description": "Stand-up",
            "description_index": 1
        }

        time_registration_info = {
            "time_placeholder_identifier": None,
            "time_value": self.time_registration_info_end_time or '09:45',

            "select_id_1": 's2id_autogen18',
            "search_bar_id_1": 's2id_autogen19_search',
            "search_bar_value_1": '24001',

            "select_id_2": 's2id_autogen20',
            "search_bar_id_2": 's2id_autogen21_search',
            "search_bar_value_2": 'Bijwerken eigen tijdregistratie',

            "description": "Bijwerken eigen tijdregistratie",
            "description_index": 2
        }

        # Enter the time, project data and description for the first row of time registration
        self.click_and_enter_value(preparation_info['select_id_1'], preparation_info['search_bar_id_1'],
                                   preparation_info['search_bar_value_1'])

        # Enter the time, project data and description for the first second of time registration

        # Enter the time, project data and description for the first third of time registration

    def click_and_enter_value(self, container_id, searchbar_id, value):
        # first open container
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, container_id))).click()

        # then enter value in the searchbar of the container
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, searchbar_id)))
        element.clear()
        element.send_keys(value)
        time.sleep(1)
        element.send_keys(Keys.ENTER)


