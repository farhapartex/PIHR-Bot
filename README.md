# PI HR Bot
This bot can be used to make attendance as an employee of PI HR system

## Features
* Make attendance for `get in` & `get out`
* Change time for `get in` & `get out`
* Pause any feature of making attendance between `get in` & `get out`

### Some prerequisite:
* Python ">=3.6"
* virtual environment
* celery
* RabbitMQ

### Installation:
To use this bot, you have to follow one time installation process. It may take few times.

* Clone this project & navigate to the root folder
* In the root folder install virtual environment. (It is your choice that, how you want to use virtual environment. If you are familiar with `pipenv`, just run `pipenv install`. It will install all packages, will create virtual environment & start it. Otherwise after creating virtual environment, install all packages from requirements.txt file)
* Run this command to start the bot! `python3 init.py run`
* First time this bot will ask your username & password of PI HR. Don't be panic, it will not be uploaded anywhere. Provide all of those. This is one time installation.

### Choose & download your browser driver
This bot use headless browser driver. So you need to download your own driver. You can select which browser you want to use. From below link choose your one's
* For chrome navigate to this [Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* For Firefox navigate to this [Firefox](https://github.com/mozilla/geckodriver/releases)
* For Edge navigate to this [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* For Safari navigate to this [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

Before downloading your browser driver, don't forget to choose your os and browser version. Suppose you want to use google chrome browse. Then check version of google chrome of your computer.
Now create a folder named with `driver` and keep your browser driver in this `driver` folder. **Please don't put your downloaded browser driver out of driver folder, otherwise it raise an error!**

### Install RabbitMQ
Install RabbitMQ from this link [RabbitMQ](https://www.rabbitmq.com/download.html). For linux ubuntu user, open terminal and run commands from bellow to install `RabbitMQ`:
* `sudo apt-get install rabbitmq-server`
* `sudo rabbitmqctl add_user myuser mypassword`
* `sudo rabbitmqctl add_vhost myvhost`
* `sudo rabbitmqctl set_user_tags myuser mytag`
* `sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"`

Substitute in appropriate values for `myuser`, `mypassword` and `myvhost` above

Installation complete! Now let's use this bot.
Open your terminal and run `sudo rabbitmq-server` which will start RabbitMQ server. Open another terminal in the root folder and run `python3 play.py` which will turn on the bot.
Every morning at 10:00AM it will give your attendance & every afternoon at 5:30PM it will set your out time.


## Advance options
By default this bot make attendance every morning at `10:00 am` & every evening at `6:00 pm`. It is very natural that this time is quite different for yours. So you can change the time schedule. To do this follow below commands
* Check is your virtual environment is running or not. If it is not running, turn it on
* in project root folder run `python3 init.py timechange`
* provide `in time` & `out time` with this format `hh:mm am/pm`
* that's all!
* run `python3 init.py run` to start this bot again!

