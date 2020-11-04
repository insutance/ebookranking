import os
from selenium import webdriver
from index.models import TotalBooks, Book

def total_books_data_insert():
    print('total_books_data_insert() start!!')
    total_books = TotalBooks.objects.all()

    rank = 1
    for book in total_books:
        ridibooks_data = Book.objects.filter(bookstore="ridibooks", title=book.title).first()
        naver_data = Book.objects.filter(bookstore="naver", title=book.title).first()
        aladin_data = Book.objects.filter(bookstore="aladin", title=book.title).first()
        yes24_data = Book.objects.filter(bookstore="yes24", title=book.title).first()
        kyobo_data = Book.objects.filter(bookstore="kyobo", title=book.title).first()

        if ridibooks_data is not None:
            book.ridibooksPrice = ridibooks_data.price
            book.author = ridibooks_data.author
            book.ridibooksLink = ridibooks_data.link
            book.image = ridibooks_data.image

        if naver_data is not None:
            book.naverPrice = naver_data.price
            book.author = naver_data.author
            book.naverLink = naver_data.link
            book.image = naver_data.image

        if aladin_data is not None:
            book.aladinPrice = aladin_data.price
            book.author = aladin_data.author
            book.aladinLink = aladin_data.link
            book.image = aladin_data.image

        if yes24_data is not None:
            book.yes24Price = yes24_data.price
            book.author = yes24_data.author
            book.yes24Link = yes24_data.link
            book.image = yes24_data.image

        if kyobo_data is not None:
            book.kyoboPrice = kyobo_data.price
            book.author = kyobo_data.author
            book.kyoboLink = kyobo_data.link
            book.image = kyobo_data.image
        
        book.rank = rank
        rank = rank+1

        book.save()
    
    return True

"""
main
"""
def total_book():
    print("**********totalbooks 시작**********")
    books = Book.objects.all()
    
    titles = []
    for book in books:
        titles.append(book.title)
    
    titles = list(set(titles))
    total_weight = {}   #total dictionary 생성

    for title in titles:
        weight = 0
        title_data = []

        kyobo_book = Book.objects.filter(bookstore='kyobo', title=title).first()
        yes24_book = Book.objects.filter(bookstore='yes24', title=title).first()
        aladin_book = Book.objects.filter(bookstore='aladin', title=title).first()
        naver_book = Book.objects.filter(bookstore='naver', title=title).first()
        ridibooks_book = Book.objects.filter(bookstore='ridibooks', title=title).first()

        if kyobo_book is not None:
            weight += kyobo_book.weight
        if yes24_book is not None:
            weight += yes24_book.weight
        if aladin_book is not None:
            weight += aladin_book.weight
        if naver_book is not None:
            weight += naver_book.weight
        if ridibooks_book is not None:
            weight += ridibooks_book.weight
        
        total_weight[title] = weight

    total_weight = sorted(total_weight.items(), key=lambda item: item[1], reverse=True)

    print('title and weight store start!!')
    for title, weight in total_weight:
        TotalBooks(title=title, weight=weight).save()
    
    total_books_data_insert()

    print("**********Totalbooks 완료**********")
    return True