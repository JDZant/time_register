from datetime import datetime, timedelta

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TimeRegistration:
    def __init__(self, driver, start_time):
        self.driver = driver

        # Set default time values (minutes)
        self.preparation_info_time = 30
        self.standup_info_time = 30
        self.time_registration_info_time = 15

        # default time between placeholders (hours)
        self.placeholder_interval = 1

        # set time registration arrays

        # preparation_info is the only array that needs start_time_placeholder_id.
        # After that the start_times are based off the end times of the previous entry
        preparation_info = {
            "start_placeholder_id": '08:30',
            "end_placeholder_id": self.calculate_time(start_time, 'hours', self.placeholder_interval),

            "start_time_value": start_time or '08:30',
            "end_time_value": self.calculate_time(start_time, 'minutes', self.preparation_info_time),

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
            "end_placeholder_id": self.calculate_time(preparation_info['end_time_value'], 'hours',
                                                      self.placeholder_interval),

            "end_time_value": self.calculate_time(preparation_info['end_time_value'], 'minutes',
                                                  self.standup_info_time),

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
            "end_placeholder_id": self.calculate_time(standup_info['end_time_value'], 'hours',
                                                      self.placeholder_interval),

            "end_time_value": self.calculate_time(standup_info['end_time_value'],
                                                  'minutes', self.time_registration_info_time),

            "select_id_1": 's2id_autogen18',
            "search_bar_id_1": 's2id_autogen19_search',
            "search_bar_value_1": '24001',

            "select_id_2": 's2id_autogen20',
            "search_bar_id_2": 's2id_autogen21_search',
            "search_bar_value_2": 'Bijwerken eigen tijdregistratie',

            "description": "Bijwerken eigen tijdregistratie",
            "description_index": 2
        }

        # first entry
        self.enter_time(preparation_info['start_placeholder_id'], preparation_info['start_time_value'])
        self.enter_time(preparation_info['end_placeholder_id'], preparation_info['end_time_value'])

        self.click_and_enter_value(preparation_info['select_id_1'], preparation_info['search_bar_id_1'],
                                   preparation_info['search_bar_value_1'])

        self.click_and_enter_value(preparation_info['select_id_2'], preparation_info['search_bar_id_2'],
                                   preparation_info['search_bar_value_2'])

        self.enter_description_info(preparation_info['description'], preparation_info['description_index'])

        # second entry
        self.enter_time(standup_info['end_placeholder_id'], standup_info['end_time_value'])

        self.click_and_enter_value(standup_info['select_id_1'], standup_info['search_bar_id_1'],
                                   standup_info['search_bar_value_1'])

        self.click_and_enter_value(standup_info['select_id_2'], standup_info['search_bar_id_2'],
                                   standup_info['search_bar_value_2'])

        self.enter_description_info(standup_info['description'], standup_info['description_index'])

        # third entry
        self.enter_time(time_registration_info['end_placeholder_id'], time_registration_info['end_time_value'])

        self.click_and_enter_value(time_registration_info['select_id_1'], time_registration_info['search_bar_id_1'],
                                   time_registration_info['search_bar_value_1'])

        self.click_and_enter_value(time_registration_info['select_id_2'], time_registration_info['search_bar_id_2'],
                                   time_registration_info['search_bar_value_2'])

        self.enter_description_info(time_registration_info['description'], time_registration_info['description_index'])

    def click_and_enter_value(self, container_id, searchbar_id, value):
        # first open container
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, container_id))).click()

        # then enter value in the searchbar of the container
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, searchbar_id)))
        element.clear()
        element.send_keys(value)
        time.sleep(1)
        element.send_keys(Keys.ENTER)

    def enter_time(self, id, time_value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            f"input.form-control.time-field[placeholder='{id}']")))
        element.clear()
        element.send_keys(time_value)
        time.sleep(1)
        element.send_keys(Keys.TAB)

    @staticmethod
    def calculate_time(time_value, format_value, integer_value):
        # Convert start_time to a datetime object
        start_time_obj = datetime.strptime(time_value, "%H:%M")

        # Prepare the time delta arguments
        time_delta_args = {format_value: integer_value}

        # Add one hour to start_time_obj
        result_time_obj = start_time_obj + timedelta(**time_delta_args)

        # Format end_time_obj back to a string and return it
        return result_time_obj.strftime("%H:%M")

    def enter_description_info(self, description_text, input_index):
        description_fields = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//input[@type="text"][@placeholder="description"][@ng-model="model.description"]'))
        )
        if 0 <= input_index < len(description_fields):
            description_field = description_fields[input_index]
            description_field.clear()
            description_field.send_keys(description_text)
        else:
            raise IndexError("Input index out of range")
