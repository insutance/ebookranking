from selenium import webdriver
from . import crawling_kyobo, crawling_yes24, crawling_aladin, crawling_naver, crawling_ridibooks
from index.models import TotalBooks, Book

def total_books_data_insert():
    total_books = TotalBooks.objects.all()

    rank = 1
    for book in total_books:
        if Book.objects.filter(bookstore="ridibooks", title=book.title).first() is not None:
            ridibooks_data = Book.objects.filter(bookstore="ridibooks", title=book.title).first()
            book.ridibooksPrice = ridibooks_data.price
            book.author = ridibooks_data.author
            book.ridibooksLink = ridibooks_data.link
            book.image = ridibooks_data.image

        if Book.objects.filter(bookstore="naver", title=book.title).first() is not None:
            naver_data = Book.objects.filter(bookstore="naver", title=book.title).first()
            book.naverPrice = naver_data.price
            book.author = naver_data.author
            book.naverLink = naver_data.link
            book.image = naver_data.image

        if Book.objects.filter(bookstore="aladin", title=book.title).first() is not None:
            aladin_data = Book.objects.filter(bookstore="aladin", title=book.title).first()
            book.aladinPrice = aladin_data.price
            book.author = aladin_data.author
            book.aladinLink = aladin_data.link
            book.image = aladin_data.image

        if Book.objects.filter(bookstore="yes24", title=book.title).first() is not None:
            yes24_data = Book.objects.filter(bookstore="yes24", title=book.title).first()
            book.yes24Price = yes24_data.price
            book.author = yes24_data.author
            book.yes24Link = yes24_data.link
            book.image = yes24_data.image

        if Book.objects.filter(bookstore="kyobo",title=book.title).first() is not None:
            kyobo_data = Book.objects.filter(bookstore="kyobo", title=book.title).first()
            book.kyoboPrice = kyobo_data.price
            book.author = kyobo_data.author
            book.kyoboLink = kyobo_data.link
            book.image = kyobo_data.image
        
        book.rank = rank
        rank = rank+1

        book.save()

"""
main
"""
def total_books():
    print("totalbooks 시작")
    options = webdriver.ChromeOptions()  # option 생성
    options.add_argument('headless')  # 창 안띄우게 하는 옵션 추가
    options.add_argument("--disable-gpu")  # gpu 사용 안 한다는거
    options.add_argument("lang=ko_KR")  # 한국어로 설정
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")  # UserAgent 탐지를 막기 위해

    driver = webdriver.Chrome('/Users/insutance/Downloads/chromedriver',options=options)  # options는 우리가 추가한 옵션 추가해주기 위해 넣음

    kyobo_dic = crawling_kyobo.kyobo(driver)
    yes24_dic = crawling_yes24.yes24(driver)
    aladin_dic = crawling_aladin.aladin(driver)
    naver_dic = crawling_naver.naver(driver)
    ridibooks_dic = crawling_ridibooks.ridibooks(driver)

    driver.quit()
    print("driver quit")

    total_titles = list(kyobo_dic.keys()) + list(yes24_dic.keys()) + list(aladin_dic.keys()) + list(naver_dic.keys()) + list(ridibooks_dic.keys())
    total_titles = list(set(total_titles))  # set을 사용하여 중복값 제거

    total_weight = {}   #total dictionary 생성

    for title in total_titles:
        weight = 0
        title_data = []
        if (title in kyobo_dic.keys()):
            weight += kyobo_dic[title][0]
        if (title in yes24_dic.keys()):
            weight += yes24_dic[title][0]
        if (title in aladin_dic.keys()):
            weight += aladin_dic[title][0]
        if (title in naver_dic.keys()):
            weight += naver_dic[title][0]
        if (title in ridibooks_dic.keys()):
            weight += ridibooks_dic[title][0]

        total_weight[title] = weight
    
    total_weight = sorted(total_weight.items(), key=lambda item: item[1], reverse=True)
    
    for title, weight in total_weight:
        TotalBooks(title=title, weight=weight).save()
    
    total_books_data_insert()

    print("Totalbooks 완료")
'''
for key, value in total_weight:
    print(key + ': ' + str(value))
'''


