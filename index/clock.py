import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ebookranking.settings'

import django
django.setup()

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from index.models import TotalBooks, Book
from index.crawling import crawling_kyobo,crawling_yes24,crawling_aladin,crawling_naver,crawling_ridibooks,crawling_totalbook
import time
"""
def crawling_job():
    for i in range(10):
        while True:
            try:
                Book.objects.all().delete()
                TotalBooks.objects.all().delete()
                
                crawling_kyobo.kyobo()
                crawling_yes24.yes24()
                crawling_aladin.aladin()
                crawling_naver.naver()
                crawling_ridibooks.ridibooks()
                crawling_totalbook.total_book()
            except Exception as e:
                print("Error 발생: " + e)
                continue
            break
        break


scheduler = BackgroundScheduler()
scheduler.add_job(crawling_job, 'interval', minutes=3)
scheduler.start()

while True:
    print('time sleep')
    time.sleep(10)
"""
sched = BlockingScheduler()

@sched.scheduled_job('cron', hour='*', minute='0,15,30,45')
def scheduled_job():
    for i in range(10):
        while True:
            try:
                Book.objects.all().delete()
                TotalBooks.objects.all().delete()
                
                crawling_kyobo.kyobo()
                crawling_yes24.yes24()
                crawling_aladin.aladin()
                crawling_naver.naver()
                crawling_ridibooks.ridibooks()
                crawling_totalbook.total_book()
            except Exception as e:
                print(e)
                continue
            break
        break

sched.start()
