from django.shortcuts import render, redirect
from .models import Kyobo, Yes24, Aladin, Naver, Ridibooks, TotalBooks
from db import insert_data

# Create your views here.
def index(request):
    total_books = TotalBooks.objects.all()

    for book in total_books:
        if Ridibooks.objects.filter(title=book.title).first() is not None:
            ridibooks_data = Ridibooks.objects.filter(title=book.title).first()
            book.ridibooksPrice = ridibooks_data.price
            book.author = ridibooks_data.author
            book.ridibooksLink = ridibooks_data.link
            book.image = ridibooks_data.image
            book.save()

        if Naver.objects.filter(title=book.title).first() is not None:
            naver_data = Naver.objects.filter(title=book.title).first()
            book.naverPrice = naver_data.price
            book.author = naver_data.author
            book.naverLink = naver_data.link
            book.image = naver_data.image
            book.save()

        if Aladin.objects.filter(title=book.title).first() is not None:
            aladin_data = Aladin.objects.filter(title=book.title).first()
            book.aladinPrice = aladin_data.price
            book.author = aladin_data.author
            book.aladinLink = aladin_data.link
            book.image = aladin_data.image
            book.save()

        if Yes24.objects.filter(title=book.title).first() is not None:
            yes24_data = Yes24.objects.filter(title=book.title).first()
            book.yes24Price = yes24_data.price
            book.author = yes24_data.author
            book.yes24Link = yes24_data.link
            book.image = yes24_data.image
            book.save()

        if Kyobo.objects.filter(title=book.title).first() is not None:
            kyobo_data = Kyobo.objects.filter(title=book.title).first()
            book.kyoboPrice = kyobo_data.price
            book.author = kyobo_data.author
            book.kyoboLink = kyobo_data.link
            book.image = kyobo_data.image
            book.save()

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
    return redirect('index')

def insert(request):
    insert_data()
    return redirect('index')

def test(request):
    return render(request, 'test.html')
