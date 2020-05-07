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
This bot use headless browser driver. So you need to download your own driver. You need to select chrome browser driver. From below link choose your one's
* For chrome navigate to this [Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Before downloading your browser driver, don't forget to choose your os and browser version. For browser version, check version of google chrome of your computer.
Now create a folder named with `driver` and keep your browser driver in this `driver` folder. **Please don't put your downloaded browser driver out of driver folder, otherwise it raise an error!**

### Install RabbitMQ
Install RabbitMQ from this link [RabbitMQ](https://www.rabbitmq.com/download.html). For linux ubuntu user, open terminal and run commands from bellow to install `RabbitMQ`:
* `sudo apt-get install rabbitmq-server`
* `sudo rabbitmqctl add_user myuser mypassword`
* `sudo rabbitmqctl add_vhost myvhost`
* `sudo rabbitmqctl set_user_tags myuser mytag`
* `sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"`

Substitute in appropriate values for `myuser`, `mypassword` and `myvhost` above

#### Installation complete! Now let's use this bot.
Open your terminal and run `sudo rabbitmq-server` which will start RabbitMQ server. Open another terminal in the root folder and run `python3 init.py run` which will turn on the bot.
Initially every morning at 10:00AM it will give your attendance, get out attendacne will be paused and weekend days weill be on Saturday & Sunday.
But don't worry! You can modify features! 


## Advance options

### Time schedule change
By default this bot make attendance every morning at `9:00 am` & every evening at `6:00 pm`. It is very natural that this time is quite different for yours. So you can change the time schedule. To do this follow below commands
* Check is your virtual environment is running or not. If it is not running, **turn it on**
* in project root folder run `python3 init.py timechange`
* provide `in time` & `out time` with this format `hh:mm am/pm`
* that's all!
* run `python3 init.py run` to start this bot again!

### Pause get_in or get_out attendance feature
You can pause get in or get out attendance feature. To do any of this run bellow commands:
* to pause get in feature run `python3 init.py get_in_down`
* to turn on get in feature run `python3 init.py get_in_up`
* to turn on get out feature run `python3 init.py get_out_up`
* to pause get out feature run `python3 init.py get_out_down`