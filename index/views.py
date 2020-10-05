from django.shortcuts import render, redirect
from .models import Book, TotalBooks
from .crawling.crawling_totalbooks import total_books
from django.utils import timezone

# Create your views here.
def index(request):
    books = TotalBooks.objects.all()
    return render(request, 'index.html', {'totalbooks': books})

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
    total_books()
    return redirect('index')

def search(request):
    if request.method=="POST":
        keyword = request.POST['keyword']
        datas = TotalBooks.objects.filter(title__icontains=keyword)
        return render(request, 'search.html', {"keyword": keyword, "datas": datas})

def test(request):
    return render(request, 'test.html')
