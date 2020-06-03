from django.db import models
from django.utils import timezone

# Create your models here.
class Kyobo(models.Model):
    title = models.CharField(max_length = 100)
    price = models.IntegerField()
    link = models.URLField()
    author = models.CharField(max_length = 100)
    image = models.URLField()

    def __str__(self):
        return self.title

class Yes24(models.Model):
    title = models.CharField(max_length = 100)
    price = models.IntegerField()
    link = models.URLField()
    author = models.CharField(max_length = 100)
    image = models.URLField()

    def __str__(self):
        return self.title

class Aladin(models.Model):
    title = models.CharField(max_length = 100)
    price = models.IntegerField()
    link = models.URLField()
    author = models.CharField(max_length = 100)
    image = models.URLField()

    def __str__(self):
        return self.title

class Naver(models.Model):
    title = models.CharField(max_length = 100)
    price = models.IntegerField()
    link = models.URLField()
    author = models.CharField(max_length = 100)
    image = models.URLField()

    def __str__(self):
        return self.title

class Ridibooks(models.Model):
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

    def __str__(self):
        return self.title
