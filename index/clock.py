import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ebookranking.settings'

import django
django.setup()

from apscheduler.schedulers.blocking import BlockingScheduler
from index.models import TotalBooks, Book
from index.crawling import crawling_kyobo,crawling_yes24,crawling_aladin,crawling_naver,crawling_ridibooks,crawling_totalbook

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour='6,12')
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
                print("Error 발생: " + e)
                continue
            break
        break

sched.start()