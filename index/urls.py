from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('kyobo', views.kyobo, name="kyobo"),
    path('delete', views.delete, name="delete"),
    path('insert', views.insert, name="insert"),
    path('test', views.test, name="test"),
]