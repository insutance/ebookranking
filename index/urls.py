from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('kyobo', views.kyobo, name="kyobo"),
    path('yes24', views.yes24, name="yes24"),
    path('aladin', views.aladin, name="aladin"),
    path('naver', views.naver, name="naver"),
    path('ridibooks', views.ridibooks, name="ridibooks"),
    path('delete', views.delete, name="delete"),
    #path('insert', views.insert, name="insert"),
    path('search', views.search, name="search"),
    path('test', views.test, name="test"),
    path('crawling-kyobo', views.crawling_kyobo, name="crawling-kyobo"),
    path('crawling-yes24', views.crawling_yes24, name="crawling-yes24"),
    path('crawling-aladin', views.crawling_aladin, name="crawling-aladin"),
    path('crawling-naver', views.crawling_naver, name="crawling-naver"),
    path('crawling-ridibooks', views.crawling_ridibooks, name="crawling-ridibooks"),
    path('crawling-totalbook', views.crawling_totalbook, name="crawling-totalbook"),
]