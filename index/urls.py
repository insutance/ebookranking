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
    path('test', views.test, name="test"),
]