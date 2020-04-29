from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import time

logger = get_task_logger(__name__)

# app = Celery("task", broker="redis://localhost:6379")
app = Celery('periodic', broker="pyamqp://guest@localhost//")

@app.task
def see_you():
    logger.info("Sent feedback email")
    print("See you in ten seconds!")


app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "task.see_you",
        "schedule": crontab(minute='*/1'),
        # 'args': (16, 16),
    }
}

# @periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
# def some_task():
#     logger.info("Sent feedback email")
#     print("See you in ten seconds!")