from pathlib import Path
import os
import os.path
# from pihrbot.bot import settings

CURRENT_DIR = os.getcwd()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_file_exists():
    return True if Path(BASE_DIR +"/setting/credentials.txt").is_file() else False

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
        with open(BASE_DIR + "/setting/credentials.txt", "a") as user_file:
            user_file.write(username+ "\n")
            user_file.write(password+ "\n")
            user_file.write(company+ "\n")
            user_file.close()
        
        set_timer()
        return True
    except:
        return False


def get_credentials():
    with open(BASE_DIR + "/setting/credentials.txt", "r") as user_file:
        username, password, company = [ch.replace("\n", "") for ch in user_file.readlines()]
        user_file.close()
        return (username, password, company)


def get_time():
    if not Path(BASE_DIR + '/pihrbot/timer.txt').is_file():
        set_timer()

    with open(BASE_DIR + "/pihrbot/timer.txt", "r") as times:
        data = [ch.replace("\n", "") for ch in times.readlines()]
        times.close()
    
    in_time, out_time = data[0], data[1]
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
        with open(BASE_DIR + "/pihrbot/timer.txt", "r+") as times:
            data = [ch.replace("\n", "") for ch in times.readlines()]
            times.seek(0)
            times.write(data[0]+ "\n")
            times.write(data[1]+ "\n")
            times.write(day1.title() + "\n")
            times.write(day2.title() + "\n")
            times.close()
        
        print("Weekend changed successfully!")
        return True
    except:
        return False


def check_driver_exists():
    try:
        return True if Path(BASE_DIR +"/driver/chromedriver").is_file() else False
    except:
        return False
