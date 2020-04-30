from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import time

logger = get_task_logger(__name__)

# app = Celery("task", broker="redis://localhost:6379")
app = Celery('periodic', broker="pyamqp://guest@localhost//")

@app.task
def login():
    logger.info("It is night 8:50")
    print("See you in user login!")

@app.task
def get_in():
    logger.info("It is night 8:52")
    print("See you in get in!")


app.conf.beat_schedule = {
    "user-login": {
        "task": "task.login",
        "schedule": crontab(hour=20, minute=50),
        'args': None,
    },
    "user-get-in": {
        "task": "task.get_in",
        "schedule": crontab(hour=20, minute=52),
        'args': None,
    }
}

app.conf.timezone = 'Asia/Dhaka'
