from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import pandas as pd, numpy as np
import datetime, time, sys

class PIHRBot:
    def __init__(self, username, password, company_name):
        self.username, self.password = username, password
        self.url = "http://{0}.pihr.xyz/Login/Index".format(company_name)
        self.chrome_driver_path = "/home/nazmul/Documents/myProjects/scrapper/pi-hr-scrapper/chromedriver"
        self.webdriver = None
        
        self.get_ready_browser()
    
    
    def get_ready_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        self.webdriver = webdriver.Chrome(
            executable_path=self.chrome_driver_path,
            options = chrome_options
            )
    
    def get_in_time(self):
        now = datetime.datetime.now()
        return now.replace(hour=10, minute=0, second=0, microsecond=0)
    
    def get_out_time(self):
        now = datetime.datetime.now()
        return now.replace(hour=17, minute=30, second=0, microsecond=0)
    
    def give_attendence(self, mission=None):
        with self.webdriver as driver:
            wait = WebDriverWait(driver, 10)
            print("Mission started! Wait...")
            driver.get(self.url)
            # get fields
            username_field = driver.find_element_by_id("UserName")
            password_field = driver.find_element_by_id("Password")
            submit_button = driver.find_element_by_id("btn-login")
            # set value to fields
            username_field.send_keys(self.username)
            password_field.send_keys(self.password)
            submit_button.click()
            
            
            wait.until(presence_of_element_located((By.CSS_SELECTOR, ".profile-sidebar-portlet")))
            results = driver.find_elements_by_class_name("profile-usertitle-name")
            print("Hello, {0}".format(results[0].text))
            
            if mission and mission == "in":
                set_in_button = driver.find_element_by_id("btnSetInTime")
                set_in_button.click()
                print("Good morning! Your attendence has been set!")
            elif mission and mission == "out":
                set_out_button = driver.find_element_by_id("btnSetOutTime")
                set_out_button.click()
                print("Good afternoon! Your set out time has been set!")
                
            driver.close()
        
        return True
        

if __name__ == "__main__":
    print("Welcome to PI HR Bot")
    while True:
        username = input("Enter Your username: ")
        password = input("Enter Your password: ")
        if not username or not password:
            print("Please provide username and password")
        else:
            break
    mission = input("Mission: ")
    bot = PIHRBot(username=username, password=password, company_name="strativ")
    
    if bot.give_attendence(mission):
        print("Mission is done! yeee!")
    else:
        print("It seems there are some problems. Try again!")
        
        
        