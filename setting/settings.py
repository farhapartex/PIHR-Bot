#!/usr/bin/env python3

import os
from pihrbot.files import *
from pihrbot.install import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_args(args):
    if len(args) <=1:
        print("Command is wrong. Run python3 init.py run")
    elif args[0] == "init.py" and args[1] == "run":
        try:
            if check_file_exists():
                os.chdir(BASE_DIR + "/pihrbot")
                celery = os.system("celery -A task worker --beat --loglevel=info")
            else:
                install = Install()
        except:
            print("It seems there are some problems. Try again!")
    
    elif args[0] == "init.py" and args[1] == "timechange":
        try:
            in_time = input("Type in time (format: hh:mm am/pm) ")
            out_time = input("Type out time (format: hh:mm am/pm) ")
            change_time(in_time, out_time)
        except:
            print("It seems there are some problems. Try again!")