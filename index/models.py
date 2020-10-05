from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Book(models.Model):
    bookstore = models.CharField(max_length=20)
    rank = models.IntegerField()
    title = models.CharField(max_length = 100)
    price = models.CharField(max_length=20)
    link = models.URLField()
    author = models.CharField(max_length = 100)
    image = models.URLField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class TotalBooks(models.Model):
    title = models.CharField(max_length = 100)
    weight = models.FloatField()    # 가중치는 실수로 저장
    author = models.CharField(max_length = 100, default='')
    image = models.URLField(default='')
    
    kyoboPrice = models.CharField(max_length=20)
    yes24Price = models.CharField(max_length=20)
    aladinPrice = models.CharField(max_length=20)
    naverPrice = models.CharField(max_length=20)
    ridibooksPrice = models.CharField(max_length=20)

    kyoboLink = models.URLField(default='')
    yes24Link = models.URLField(default='')
    aladinLink = models.URLField(default='')
    naverLink = models.URLField(default='')
    ridibooksLink = models.URLField(default='')

    rank = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title