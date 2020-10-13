import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ebookranking.settings'

import django
django.setup()

from apscheduler.schedulers.blocking import BlockingScheduler
from index.models import TotalBooks, Book
from index.crawling import crawling_kyobo,crawling_yes24,crawling_aladin,crawling_naver,crawling_ridibooks,crawling_totalbook

sched = BlockingScheduler()
"""
@sched.scheduled_job('interval', minutes=2)
def crawlied_kyobo():
    Book.objects.all().delete()
    TotalBooks.objects.all().delete()
    
    crawling_kyobo.kyobo()
    crawling_yes24.yes24()
    crawling_aladin.aladin()
    crawling_naver.naver()
    crawling_ridibooks.ridibooks()
    crawling_totalbook.total_book()

@sched.scheduled_job('interval', minutes=3)
def crawlied_yes24():
    crawling_yes24.yes24()

@sched.scheduled_job('interval', minutes=4)
def crawlied_aladin():
    crawling_aladin.aladin()

@sched.scheduled_job('interval', minutes=5)
def crawlied_naver():
    crawling_naver.naver()

@sched.scheduled_job('interval', minutes=6)
def crawlied_ridibooks():
    crawling_ridibooks.ridibooks()

@sched.scheduled_job('interval', minutes=7)
def crawlied_totalbook():
    crawling_totalbook.total_book()
"""
@sched.scheduled_job('cron', day_of_week='mon-sun', hour='*' ,minute='0,5,10,15,20,25,30,35,40,45,50,55')
def scheduled_job():
    Book.objects.all().delete()
    TotalBooks.objects.all().delete()
    
    crawling_kyobo.kyobo()
    crawling_yes24.yes24()
    crawling_aladin.aladin()
    crawling_naver.naver()
    crawling_ridibooks.ridibooks()
    crawling_totalbook.total_book()

sched.start()