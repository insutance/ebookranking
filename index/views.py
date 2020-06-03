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
