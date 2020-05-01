from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import pandas as pd, numpy as np
import datetime, time, sys
from files import BASE_DIR, get_credentials

class PIHRBot:
    def __init__(self):
        credentials = get_credentials()
        self._username, self._password = credentials[0], credentials[1]
        self._url = "http://{0}.pihr.xyz/Login/Index".format("strativ")
        self._chrome_driver_path, self._webdriver = "", None
        self._get_ready_browser()
        self._get_login()
    
    
    def _get_ready_browser(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            self._chrome_driver_path = BASE_DIR +"/driver/chromedriver"

            self._webdriver = webdriver.Chrome(
                executable_path=self._chrome_driver_path,
                options = chrome_options
                )
        except:
            print("Driver not found!")
        
    
    def _get_login(self):
        wait = WebDriverWait(self._webdriver, 10)
        print("Mission started! Wait...")
        self._webdriver.get(self._url)
        # get fields
        username_field = self._webdriver.find_element_by_id("UserName")
        password_field = self._webdriver.find_element_by_id("Password")
        submit_button = self._webdriver.find_element_by_id("btn-login")
        # set value to fields
        username_field.send_keys(self._username)
        password_field.send_keys(self._password)
        submit_button.click()
          
        wait.until(presence_of_element_located((By.CSS_SELECTOR, ".profile-sidebar-portlet")))
        
    
    def get_in(self):
        results = self._webdriver.find_elements_by_class_name("profile-usertitle-name")
        print("Good morning! Your attendence has been set!")

        # self.webdriver.close()
    def get_out(self):
        results = self._webdriver.find_elements_by_class_name("profile-usertitle-name")
        print("Good afternoon! Your set out time has been set!")
    
    def driver_close(self):
        self._webdriver.close()
        
        return True
        
    
    