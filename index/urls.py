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
    path('insert', views.insert, name="insert"),
    path('search', views.search, name="search"),
    path('test', views.test, name="test"),
    path('crawling/kyobo', views.crawlingKyobo, name="crawling_kyobo"),
    path('crawling/yes24', views.crawlingYes24, name="crawling_yes24"),
    path('crawling/aladin', views.crawlingAladin, name="crawling_aladin"),
    path('crawling/naver', views.crawlingNaver, name="crawling_naver"),
    path('crawling/ridibooks', views.crawlingRidibooks, name="crawling_ridibooks"),
    path('crawling/totalbook', views.crawlingTotalbook, name="crawling_totalbook"),
    path('delete/kyobo', views.deleteKyobo, name="delete_kyobo"),
    path('delete/yes24', views.deleteYes24, name="delete_yes24"),
    path('delete/aladin', views.deleteAladin, name="delete_aladin"),
    path('delete/naver', views.deleteNaver, name="delete_naver"),
    path('delete/ridibooks', views.deleteRidibooks, name="delete_ridibooks"),
    path('delete/totalbook', views.deleteTotalBook, name="delete_totalbook"),
]