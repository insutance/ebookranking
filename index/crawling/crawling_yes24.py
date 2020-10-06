import os
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from index.models import Book

def crawling_init():
    print("예스24 크롤링 시작")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    #driver = webdriver.Chrome('/Users/insutance/Downloads/chromedriver',options=chrome_options)  # options는 우리가 추가한 옵션 추가해주기 위해 넣음

    driver.get('http://www.yes24.com/24/Category/BestSeller?CategoryNumber=017&sumgb=06&AO=4&FetchSize=50')  # FetchSize 가 한번에 뜨는 책 개수
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
        list[n] = list[n].replace(",","")
        list[n] = list[n].replace("원", "")
        list[n] = list[n].strip()
        list[n] = int(list[n])
    return list

def clearAuthor(list):
    for n in range(len(list)):
        index = 0
        for m in range(len(list[n])):
            if list[n][m] == '저':
                index = m
                break

        list[n] = list[n][1:index-1]  # 0번째 index가 '\n' , index-1 하는 이유는 맨 마지막에 공백이 존재함.
        list[n].strip()

    return list
'''
Main Code
'''
def yes24():
    soup = crawling_init()

    titles = []     # 제목 저장 리스트
    prices = []     # 가격 저장 리스트
    links = []      # 링크 저장 리스트
    authors = []    # 저자 저장 리스트
    images = []     # 이미지 저장 리스트

    n = 1
    while(len(titles) < 30):
        title = soup.select_one('#category_layout > tbody > tr:nth-child(' + str(n) + ') > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)')  # select_one을 통해 각 제목 얻어와 title에 저장
        price = soup.select_one('#category_layout > tbody > tr:nth-child(' + str(n) + ') > td.goodsTxtInfo > p:nth-child(3) > span.priceB')
        author = soup.select_one('#category_layout > tbody > tr:nth-child(' + str(n) + ') > td.goodsTxtInfo > div')
        image = soup.select_one('#category_layout > tbody > tr:nth-child(' + str(n) + ') > td.image > div > a:nth-child(1) > img')

        if (title is None or price is None):
            continue
        elif ("크레마" in title.text):
            n += 2
            continue
        else:
            titles.append(title.text)  # 저장된 title을 titles 리스트에 저장
            prices.append(price.text)
            links.append("http://www.yes24.com" + title.get('href'))  # title에서 가져올수 있음.
            authors.append(author.text)
            images.append(image.get('src'))

        n += 2

    titles = clearTitle(titles)
    prices = clearPrice(prices)
    authors = clearAuthor(authors)

    dic_price = {}
    dic_weight = {}

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
        Book(title=title, bookstore="yes24", weight=value[0],price=value[1], link=value[2], author=value[3], image=value[4], rank=value[5]).save()

    print("예스24 크롤링 완료")
    #return data
    return True