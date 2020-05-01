from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import time
from bot import PIHRBot

logger = get_task_logger(__name__)

# app = Celery("task", broker="redis://localhost:6379")
app = Celery('periodic', broker="pyamqp://guest@localhost//")
bot = PIHRBot()

@app.task
def get_in():
    bot.get_in()
    # bot.driver_close()

@app.task
def get_out():
    bot.get_out()


app.conf.beat_schedule = {
    "user-login": {
        "task": "task.get_in",
        "schedule": crontab(hour=13, minute=14),
        'args': None,
    },
    "user-get-in": {
        "task": "task.get_out",
        "schedule": crontab(hour=13, minute=16),
        'args': None,
    }
}

app.conf.timezone = 'Asia/Dhaka'
