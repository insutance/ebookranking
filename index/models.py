from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    bookstore = models.CharField(max_length=20)
    title = models.CharField(max_length = 100)
    price = models.IntegerField()
    link = models.URLField()
    author = models.CharField(max_length = 100)
    image = models.URLField()

    def __str__(self):
        return self.title
    
class TotalBooks(models.Model):
    title = models.CharField(max_length = 100)
    weight = models.FloatField()    # 가중치는 실수로 저장
    author = models.CharField(max_length = 100, default='')
    image = models.URLField(default='')
    
    kyoboPrice = models.IntegerField(default=0)
    yes24Price = models.IntegerField(default=0)
    aladinPrice = models.IntegerField(default=0)
    naverPrice = models.IntegerField(default=0)
    ridibooksPrice = models.IntegerField(default=0)

    kyoboLink = models.URLField(default='')
    yes24Link = models.URLField(default='')
    aladinLink = models.URLField(default='')
    naverLink = models.URLField(default='')
    ridibooksLink = models.URLField(default='')

    def __str__(self):
        return self.title