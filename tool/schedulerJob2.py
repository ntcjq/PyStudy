from fake_useragent import UserAgent
from tqdm import tqdm
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time
from datetime import datetime
from datetime import date


def say(text):
    print(text)


def test():
    scheduler = BackgroundScheduler()
    ping_baidu = {
        "id": "ping_baidu",
        "func": say,
        "args": ["baidu.com"],
        "trigger": "interval",
        "seconds": 3,
    }

    scheduler.add_job(**ping_baidu)

    scheduler.add_job(say, "interval", seconds=2, args=["text"], id="job1")
    print("prepare")
    scheduler.start()
    print("start")
    time.sleep(10)
    job1 = scheduler.get_job("job1")
    if job1:
        scheduler.remove_job("job1")
        print("delete")
    print("sleep")
    time.sleep(10)
    scheduler.shutdown()
    print("end")


if __name__ == "__main__":
    test()
