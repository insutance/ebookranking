from django.shortcuts import render, redirect
from .models import Book, TotalBooks
from db import insert_data

# Create your views here.
def index(request):
    total_books = TotalBooks.objects.all()

    for book in total_books:
        if Book.objects.filter(bookstore="ridibooks", title=book.title).first() is not None:
            ridibooks_data = Book.objects.filter(bookstore="ridibooks", title=book.title).first()
            book.ridibooksPrice = ridibooks_data.price
            book.author = ridibooks_data.author
            book.ridibooksLink = ridibooks_data.link
            book.image = ridibooks_data.image
            book.save()

        if Book.objects.filter(bookstore="naver", title=book.title).first() is not None:
            naver_data = Book.objects.filter(bookstore="naver", title=book.title).first()
            book.naverPrice = naver_data.price
            book.author = naver_data.author
            book.naverLink = naver_data.link
            book.image = naver_data.image
            book.save()

        if Book.objects.filter(bookstore="aladin", title=book.title).first() is not None:
            aladin_data = Book.objects.filter(bookstore="aladin", title=book.title).first()
            book.aladinPrice = aladin_data.price
            book.author = aladin_data.author
            book.aladinLink = aladin_data.link
            book.image = aladin_data.image
            book.save()

        if Book.objects.filter(bookstore="yes24", title=book.title).first() is not None:
            yes24_data = Book.objects.filter(bookstore="yes24", title=book.title).first()
            book.yes24Price = yes24_data.price
            book.author = yes24_data.author
            book.yes24Link = yes24_data.link
            book.image = yes24_data.image
            book.save()

        if Book.objects.filter(bookstore="kyobo",title=book.title).first() is not None:
            kyobo_data = Book.objects.filter(bookstore="kyobo", title=book.title).first()
            book.kyoboPrice = kyobo_data.price
            book.author = kyobo_data.author
            book.kyoboLink = kyobo_data.link
            book.image = kyobo_data.image
            book.save()

    return render(request, 'index.html', {'totalbooks': total_books})

def kyobo(request):
    kyobos = Book.objects.filter(bookstore="kyobo")
    return render(request, 'kyobo.html', {'kyobos':kyobos})

def yes24(request):
    yes24s = Book.objects.filter(bookstore="yes24")
    return render(request, 'yes24.html', {'yes24s':yes24s})

def aladin(request):
    aladins = Book.objects.filter(bookstore="aladin")
    return render(request, 'aladin.html', {'aladins':aladins})

def naver(request):
    navers = Book.objects.filter(bookstore="naver")
    return render(request, 'naver.html', {'navers':navers})

def ridibooks(request):
    ridibooks = Book.objects.filter(bookstore="ridibooks")
    return render(request, 'ridibooks.html', {'ridibooks':ridibooks})

def delete(request):
    Book.objects.all().delete()
    TotalBooks.objects.all().delete()
    return redirect('index')

def insert(request):
    insert_data()
    return redirect('index')

def test(request):
    return render(request, 'test.html')
