from datetime import datetime, timedelta

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TimeRegistration:
    def __init__(self, driver, user_config):
        self.driver = driver

        # Default time between placeholders (hours)
        self.placeholder_interval = 1

        # Set time registration arrays

        # Preparation_info is the only array that needs start_time_placeholder_id.
        # After that the start_times are based off the end times of the previous entry
        preparation_data = {
            "start_placeholder_id": '08:30',
            "end_placeholder_id": self.calculate_time(user_config['start_time'],
                                                      'hours', self.placeholder_interval),

            "start_time_value": user_config['start_time'],
            "end_time_value": self.calculate_time(user_config['start_time'], 'minutes',
                                                  user_config['preparation_duration']),

            "select_id_1": 's2id_autogen1',
            "search_bar_id_1": 's2id_autogen2_search',
            "search_bar_value_1": '24005',

            "select_id_2": 's2id_autogen3',
            "search_bar_id_2": 's2id_autogen4_search',
            "search_bar_value_2": 'Overige werkzaamheden (specificeer)',

            "description": "Opstarten pc/laptop, klaarzetten werkomgeving, dag voorbereiden",
            "description_index": 0
        }

        standup_data = {
            "end_placeholder_id": self.calculate_time(preparation_data['end_time_value'], 'hours',
                                                      self.placeholder_interval),

            "end_time_value": self.calculate_time(preparation_data['end_time_value'], 'minutes',
                                                  user_config['standup_duration']),

            "select_id_1": 's2id_autogen5',
            "search_bar_id_1": 's2id_autogen6_search',
            "search_bar_value_1": '24005',

            "select_id_2": 's2id_autogen7',
            "search_bar_id_2": 's2id_autogen8_search',
            "search_bar_value_2": 'Vergaderen en stand-up',

            "description": "Stand-up",
            "description_index": 1
        }

        time_registration_data = {
            "end_placeholder_id": self.calculate_time(standup_data['end_time_value'], 'hours',
                                                      self.placeholder_interval),

            "end_time_value": self.calculate_time(standup_data['end_time_value'],
                                                  'minutes', user_config['time_registration_duration']),

            "select_id_1": 's2id_autogen18',
            "search_bar_id_1": 's2id_autogen19_search',
            "search_bar_value_1": '24001',

            "select_id_2": 's2id_autogen20',
            "search_bar_id_2": 's2id_autogen21_search',
            "search_bar_value_2": 'Bijwerken eigen tijdregistratie',

            "description": "Bijwerken eigen tijdregistratie",
            "description_index": 2
        }

        # Call the functions to start the time registration
        self.start_time_registration(preparation_data)
        self.start_time_registration(standup_data)
        self.start_time_registration(time_registration_data)

        # Press the save button
        self.click_save_button()

    def start_time_registration(self, data):
        # Check if 'start_placeholder_id' and 'start_time_value' are present in the data.
        # If they are, use them; otherwise, fall back to 'end_placeholder_id' and 'end_time_value'.
        if 'start_placeholder_id' in data and 'start_time_value' in data:
            self.enter_time(data['start_placeholder_id'], data['start_time_value'])

        # 'end_placeholder_id' and 'end_time_value' are expected to be present in all entries.
        self.enter_time(data['end_placeholder_id'], data['end_time_value'])

        # Proceed with the rest of the registration process.
        self.click_and_enter_value(data['select_id_1'], data['search_bar_id_1'], data['search_bar_value_1'])
        self.click_and_enter_value(data['select_id_2'], data['search_bar_id_2'], data['search_bar_value_2'])
        self.enter_description_data(data['description'], data['description_index'])

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

    def enter_description_data(self, description_text, input_index):
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

    def click_save_button(self):
        # Wait for the Save button to be clickable
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save')]"))
        )
        # Click the button
        save_button.click()
        time.sleep(3)
