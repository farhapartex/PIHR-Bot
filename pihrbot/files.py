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
        df = pd.read_csv(BASE_DIR + "/credentials.csv")
        get_in, get_out = df['get_in'][0], df['get_out'][0]
        df.loc[df.get_in==get_in, 'get_in'] = in_time
        df.loc[df.get_out==get_out, 'get_out'] = out_time
        df.to_csv(os.path.join(BASE_DIR, "credentials.csv"), index=False)
        
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

def has_get_in_feature():
    try:
        df = pd.read_csv(BASE_DIR + "/credentials.csv")
        get_in_feature = df['get_in_feature'][0]
        return True if get_in_feature == "true" else False
    except:
        pass

def has_get_out_feature():
    try:
        df = pd.read_csv(BASE_DIR + "/credentials.csv")
        get_out_feature = df['get_out_feature'][0]
        return True if get_out_feature == "true" else False
    except:
        pass


def change_get_in_feature(state):
    try:
        df = pd.read_csv(BASE_DIR + "/credentials.csv")
        get_in_feature = df['get_in_feature'][0]
        df.loc[df.get_in_feature==get_in_feature, 'get_in_feature'] = state
        df.to_csv(os.path.join(BASE_DIR, "credentials.csv"), index=False)
        return True
    except:
        return False


def change_get_out_feature(state):
    try:
        df = pd.read_csv(BASE_DIR + "/credentials.csv")
        get_out_feature = df['get_out_feature'][0]
        df.loc[df.get_out_feature==get_out_feature, 'get_out_feature'] = state
        df.to_csv(os.path.join(BASE_DIR, "credentials.csv"), index=False)
        return True
    except:
        return False


def check_driver_exists():
    try:
        return True if Path(BASE_DIR +"/driver/chromedriver").is_file() else False
    except:
        return False
