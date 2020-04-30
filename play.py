from files import *
from bot import *
from install import Install
import os

if __name__ == "__main__":
    print("Welcome to PI HR Bot")
    try:
        if check_file_exists():
            # bot = PIHRBot()
            celery = os.system("celery -A task worker --beat --loglevel=info")
        else:
            install = Install()
    except:
        print("It seems there are some problems. Try again!")

            
    