import django
django.setup()

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ebookranking.settings'

from apscheduler.schedulers.blocking import BlockingScheduler
from index.crawling import crawling_kyobo

sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=2)
def crawlied_kyobo():
    crawling_kyobo.kyobo()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()