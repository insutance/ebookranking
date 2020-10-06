import os
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from index.models import Book

def crawling_init():
    print("리디북스 크롤링 시작")
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    #driver = webdriver.Chrome('/Users/insutance/Downloads/chromedriver',options=chrome_options)  # options는 우리가 추가한 옵션 추가해주기 위해 넣음
    
    driver.get('https://ridibooks.com/bestsellers/general')
    driver.implicitly_wait(2)  # 버퍼때문에 2초간 기다리게 함

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    driver.quit()
    return soup

def clearTitle(list):
    for n in range(len(list)):
        list[n] = re.sub("[\(\[].*?[\)\]]", "", list[n])
        list[n] = list[n].strip()

    return list

def clearPrice(list):
    for n in range(len(list)):
        if list[n] == "무료":         # 가격 무료있는게 있음 (가격 비교할 수 없고 int 형 못 만듦)
            list[n] = "0,0원"         # 아래 코드에서 ',' 랑 '원' 이 필요해서 0,0원으로 넣어줌
        list[n] = list[n].replace(",","")
        list[n] = list[n].replace("원","")
        list[n] = list[n].strip()
        list[n] = int(list[n])
    return list

def clearAuthor(list):
    for n in range(len(list)):
        list[n] = list[n].replace(" ","")       # 저자 긁어올 때 공백이 많음

    return list

'''
Main Code
'''
def ridibooks():
    soup = crawling_init()

    titles = []
    prices = []
    links = []
    authors = []
    images = []

    n = 3
    while(len(titles) < 30):
        title = soup.select_one('#page_best > div.book_macro_wrapper.js_book_macro_wrapper > div:nth-child(' + str(n) + ') > div.book_metadata_wrapper > h3 > a > span')  # select_one을 통해 각 제목 얻어와 title에 저장
        price = soup.select_one('#page_best > div.book_macro_wrapper.js_book_macro_wrapper > div:nth-child(' + str(n) + ') > div.book_metadata_wrapper > div > p > span')
        link = soup.select_one('#page_best > div.book_macro_wrapper.js_book_macro_wrapper > div:nth-child(' + str(n) + ') > div.book_metadata_wrapper > h3 > a')
        author = soup.select_one('#page_best > div.book_macro_wrapper.js_book_macro_wrapper > div:nth-child(' + str(n) + ') > div.book_metadata_wrapper > p.book_metadata.author')
        image = soup.select_one('#page_best > div.book_macro_wrapper.js_book_macro_wrapper > div:nth-child(' + str(n) + ') > div.book_thumbnail_wrapper > div > div > img')

        if (title is None or price is None or link is None):
            continue
        else:
            titles.append(title.text.strip())  # 저장된 title을 titles 리스트에 저장
            prices.append(price.text.strip())
            links.append("https://ridibooks.com" + link.get('href'))
            authors.append(author.text.strip())
            images.append("https:" + image.get('data-src'))

        n += 2

    titles = clearTitle(titles)
    prices = clearPrice(prices)
    authors = clearAuthor(authors)

    data = {}

    weight = 30
    rank = 1
    for n in range(len(titles)):
        title_data = []
        title_data.append(round(weight * 0.25, 2))
        title_data.append(format(prices[n],","))
        title_data.append(links[n])
        title_data.append(authors[n])
        title_data.append(images[n])
        title_data.append(rank)
        data[titles[n]] = title_data
        weight -= 1
        rank += 1

    for title,value in data.items():
        Book(title=title, bookstore="ridibooks", weight=value[0], price=value[1], link=value[2], author=value[3], image=value[4], rank=value[5]).save()

    print("리디북스 크롤링 완료")
    #return data
    return True