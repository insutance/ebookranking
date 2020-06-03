from django.shortcuts import render
from .models import Kyobo, Yes24, Aladin, Naver, Ridibooks, TotalBooks
from db import insert_data

# Create your views here.
def index(request):
    total_books = TotalBooks.objects
    return render(request, 'index.html', {'totalbooks': total_books})

def kyobo(request):
    kyobos = Kyobo.objects
    return render(request, 'kyobo.html', {'kyobos':kyobos})

def yes24(request):
    yes24s = Yes24.objects
    return render(request, 'yes24.html', {'yes24s':yes24s})

def aladin(request):
    aladins = Aladin.objects
    return render(request, 'aladin.html', {'aladins':aladins})

def naver(request):
    navers = Naver.objects
    return render(request, 'naver.html', {'navers':navers})

def ridibooks(request):
    ridibooks = Ridibooks.objects
    return render(request, 'ridibooks.html', {'ridibooks':ridibooks})

def delete(request):
    Kyobo.objects.all().delete()
    Yes24.objects.all().delete()
    Aladin.objects.all().delete()
    Naver.objects.all().delete()
    Ridibooks.objects.all().delete()
    TotalBooks.objects.all().delete()
    return render(request, 'index.html')

def insert(request):
    insert_data()
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')
