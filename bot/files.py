from pathlib import Path
import os
import os.path 

CURRENT_DIR = os.getcwd()

def check_file_exists():
    return True if Path(CURRENT_DIR +"/credentials.txt").is_file() else False

def create_and_set_credentials(username, password):
    try:
        with open(CURRENT_DIR + "/credentials.txt", "a") as user_file:
            user_file.write(username+ "\n")
            user_file.write(password+ "\n")
            user_file.close()
            return True
    except:
        return False

def get_credentials():
    with open(CURRENT_DIR + "/credentials.txt", "r") as user_file:
        username, password = [ch.replace("\n", "") for ch in user_file.readlines()]
        user_file.close()
        return (username, password)

def check_driver_exists():
    try:
        return True if Path(CURRENT_DIR +"/driver/chromedriver").is_file() else False
    except:
        return False
    