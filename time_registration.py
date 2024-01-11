from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TimeRegistration:
    def __init__(self, driver):
        self.driver = driver

    def register_time(self):
        preparation_info = {
            "time_placeholder": "09:30",
            "time_value": "09:00",

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
            "time_placeholder": "10:00",
            "time_value": "09:30",

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
            "time_placeholder": "10:30",
            "time_value": "09:45",

            "select_id_1": 's2id_autogen18',
            "search_bar_id_1": 's2id_autogen19_search',
            "search_bar_value_1": '24001',

            "select_id_2": 's2id_autogen20',
            "search_bar_id_2": 's2id_autogen21_search',
            "search_bar_value_2": 'Bijwerken eigen tijdregistratie',

            "description": "Bijwerken eigen tijdregistratie",
            "description_index": 2
        }

        self.enter_time_and_project_info(preparation_info)
        self.enter_time_and_project_info(standup_info)
        self.enter_time_and_project_info(time_registration_info)
        self.click_save_button()

    def enter_time_and_project_info(self, info):
        """Enter time and project information using a dictionary of parameters."""
        self.wait_and_clear_send_keys(By.CSS_SELECTOR,
                                      f"input.form-control.time-field[placeholder='{info['time_placeholder']}']",
                                      info['time_value'])

        self.wait_and_click(By.ID, info['select_id_1'])
        self.wait_and_clear_send_keys(By.ID, info['search_bar_id_1'], info['search_bar_value_1'], True)
        self.wait_and_click(By.ID, info['select_id_2'])
        self.wait_and_clear_send_keys(By.ID, info['search_bar_id_2'], info['search_bar_value_2'], True)
        self.enter_description_info(info['description'], info['description_index'])

    def wait_and_click(self, by, value):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value))).click()

    def wait_and_clear_send_keys(self, by, value, keys, sleep=False):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
        element.clear()
        element.send_keys(keys)
        if sleep:
            time.sleep(2)
            element.send_keys(Keys.ENTER)

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

    def click_save_button(self):
        """Clicks the save button."""
        # Wait for the Save button to be clickable
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save')]"))
        )
        # Click the button
        save_button.click()
