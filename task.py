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
    logger.info("user login")
    print("See you in user login!")

@app.task
def get_in():
    logger.info("user get in")
    print("See you in get in!")


app.conf.beat_schedule = {
    "user-login": {
        "task": "task.login",
        "schedule": crontab(minute='*/1'),
        # 'args': (16, 16),
    },
    "user-get-in": {
        "task": "task.get_in",
        "schedule": crontab(minute='*/2'),
        # 'args': (16, 16),
    }
}
