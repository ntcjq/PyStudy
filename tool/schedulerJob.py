from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time
from datetime import datetime
from datetime import date


def job_say_hello(name: str = None):
    print(f'Hello, {name}!')


def startJob():
    #BlockingScheduler: 调度器在当前进程的主线程中运行，会阻塞当前线程。
    #BackgroundScheduler: 调度器在后台线程中运行，不会阻塞当前线程。

    # 实例化一个Scheduler类，用于调度定时任务
    scheduler = BackgroundScheduler()
    '''
    触发器(trigger)
    date是最基本的一种调度，作业任务只会执行一次
    interval触发器，固定时间间隔触发
    cron 触发器，在特定时间周期性地触发，和Linux crontab格式兼容。它是功能最强大的触发器
    '''
    # 添加任务调度，触发条件为每隔10秒钟执行一次
    scheduler.add_job(job_say_hello, 'interval', seconds=10, args=["cjq"])

    scheduler.add_job(job_say_hello,
                      'date',
                      run_date=date(2023, 8, 17),
                      args=['text1'])
    scheduler.add_job(job_say_hello,
                      'date',
                      run_date=datetime(2023, 8, 17, 17, 42, 9),
                      args=['text2'])

    scheduler.add_job(job_say_hello,
                      'date',
                      run_date='2023-08-17 17:42:15',
                      id="job1",
                      args=['text3'])

    scheduler.add_job(job_say_hello, CronTrigger.from_crontab('0 0 1-15 * *'))

    # 启动任务调度
    scheduler.start()
    print("start scheduler")

    job1 = scheduler.get_job(job_id="job1")
    if job1:
        scheduler.remove_job(job_id="job1")
    time.sleep(100)
    scheduler.shutdown()
    print("end scheduler")


if __name__ == "__main__":
    startJob()
