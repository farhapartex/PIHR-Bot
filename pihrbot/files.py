from pathlib import Path
import pandas as pd
import numpy as np
import os
import os.path
# from pihrbot.bot import settings

CURRENT_DIR = os.getcwd()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_file_exists():
    return True if Path(BASE_DIR +"/credentials.csv").is_file() else False

def set_timer():
    try:
        with open(BASE_DIR + "/pihrbot/timer.txt", "a") as timer:
            timer.write("9:00 am"+ "\n")
            timer.write("6:00 pm"+ "\n")
            timer.write("Saturday"+ "\n")
            timer.write("Sunday"+ "\n")
            timer.close()
            return True
    except:
        return False

def create_and_set_credentials(username, password, company):
    try:
        label = ['username', 'password', 'company', 'get_in', 'get_out', 'weekend1', 'weekend2', 'get_in_feature', 'get_out_feature']
        data = [username, password, company, '10:00 am', '5:00 pm', 'Saturday', 'Sunday', 'true', 'false']
        df = pd.DataFrame([data], columns=label)
        df.to_csv(os.path.join(BASE_DIR, "credentials.csv"), index=False)
        return True
    except:
        return False


def get_credentials():
    try:
        df = pd.read_csv(BASE_DIR + "/credentials.csv")
        username, password, company = df['username'][0], df['password'][0], df['company'][0]
        return (username, password, company)
    except:
        pass


def get_time():

    try:
        df = pd.read_csv(BASE_DIR + "/credentials.csv")
        in_time, out_time = df['get_in'][0], df['get_out'][0]
    except:
        in_time, out_time = '10:00 am', '6:00 pm'
    
    in_time = in_time.split()
    out_time = out_time.split()

    if in_time[1] == "am" or in_time[1] == "AM":
        in_time = in_time[0]
    elif in_time[1] == "pm" or in_time[1] == "PM":
        in_time = in_time[0].split(":")
        in_time =  str(int(in_time[0])+12) + ":" + in_time[1]
    
    if out_time[1] == "am" or out_time[1] == "AM":
        out_time = out_time[0]
    elif out_time[1] == "pm" or out_time[1] == "PM":
        out_time = out_time[0].split(":")
        out_time =  str(int(out_time[0])+12) + ":" + out_time[1]

    return (in_time, out_time)


def change_time(in_time, out_time):
    try:
        with open(BASE_DIR + "/pihrbot/timer.txt", "r+") as times:
            data = [ch.replace("\n", "") for ch in times.readlines()]
            times.seek(0)
            times.write(in_time+ "\n")
            times.write(out_time+ "\n")
            times.write(data[2]+ "\n")
            times.write(data[3]+ "\n")
            times.close()
        
        print("Time changed successfully!")
        return True
    except:
        return False


def change_weekend(day1, day2):
    try:
        df = pd.read_csv(BASE_DIR + "/credentials.csv")
        weekend1, weekend2 = df['weekend1'][0], df['weekend2'][0]
        df.loc[df.weekend1==weekend1, 'weekend1'] = day1
        df.loc[df.weekend2==weekend2, 'weekend2'] = day2
        df.to_csv(os.path.join(BASE_DIR, "credentials.csv"), index=False)
        
        print("Weekend changed successfully!")
        return True
    except:
        print("There are some error!")
        return False
        

def get_weekend():
    try:
        df = pd.read_csv(BASE_DIR + "/credentials.csv")
        weekend1, weekend2 = df['weekend1'][0], df['weekend2'][0]
    except:
        weekend1, weekend2 = 'Saturday', 'Sunday'
    
    return (weekend1, weekend2)


def check_driver_exists():
    try:
        return True if Path(BASE_DIR +"/driver/chromedriver").is_file() else False
    except:
        return False
