from django.shortcuts import render, redirect
from .models import Book, TotalBooks
from .crawling.crawling_totalbooks import total_books
from django.utils import timezone
from .crawling import crawling_kyobo,crawling_yes24,crawling_aladin,crawling_naver,crawling_ridibooks,crawling_totalbook

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
    #total_books()
    crawling_ridibooks.ridibooks()
    crawling_naver.naver()
    crawling_aladin.aladin()
    crawling_yes24.yes24()
    crawling_kyobo.kyobo()
    crawling_totalbook.total_book()

    return redirect('index')

def crawlingKyobo(request):
    crawling_kyobo.kyobo()
    return redirect('kyobo')

def crawlingYes24(request):
    crawling_yes24.yes24()
    return redirect('yes24')

def crawlingAladin(request):
    crawling_aladin.aladin()
    return redirect('aladin')

def crawlingNaver(request):
    crawling_naver.naver()
    return redirect('naver')

def crawlingRidibooks(request):
    crawling_ridibooks.ridibooks()
    return redirect('ridibooks')

def crawlingTotalbook(request):
    crawling_totalbook.total_book()
    return redirect('index')

def deleteKyobo(request):
    Book.objects.filter(bookstore="kyobo").all().delete()
    return redirect('kyobo')

def deleteYes24(request):
    Book.objects.filter(bookstore="yes24").all().delete()
    return redirect('yes24')

def deleteAladin(request):
    Book.objects.filter(bookstore="aladin").all().delete()
    return redirect('aladin')

def deleteNaver(request):
    Book.objects.filter(bookstore="naver").all().delete()
    return redirect('naver')

def deleteRidibooks(request):
    Book.objects.filter(bookstore="ridibooks").all().delete()
    return redirect('ridibooks')

def deleteTotalBook(request):
    TotalBooks.objects.all().delete()
    return redirect('index')

def search(request):
    if request.method=="POST":
        keyword = request.POST['keyword']
        datas = TotalBooks.objects.filter(title__icontains=keyword)
        return render(request, 'search.html', {"keyword": keyword, "datas": datas})

def test(request):
    return render(request, 'test.html')
