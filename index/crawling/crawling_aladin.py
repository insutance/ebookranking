import os
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from index.models import Book


def crawling_init():
    print("알라딘 크롤링 시작")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    #driver = webdriver.Chrome('/Users/insutance/Downloads/chromedriver',options=chrome_options)  # options는 우리가 추가한 옵션 추가해주기 위해 넣음
    
    driver.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=9&BestType=EBookBestseller')
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
        list[n] = list[n].strip()
        list[n] = int(list[n])
    return list

def clearAuthor(list):
    for n in range(len(list)):
        index = 0
        for m in range(len(list[n])):
            if list[n][m] == '(':
                index = m
                break

        list[n] = list[n][:index-1]  # 0번째 index가 '\n' , index-1 하는 이유는 맨 마지막에 공백이 존재함.
        list[n].strip()

    return list
'''
Main Code
'''
def aladin():
    soup = crawling_init()

    titles = []     # 제목 저장 리스트
    prices = []     # 가격 저장 리스트
    links = []      # 링크 저장 리스트
    authors = []    # 저자 저장 리스트
    images = []     # 이미지 저장 리스트

    n = 3
    while(len(titles) < 30):
        title = soup.select_one('#Myform > div:nth-child(' + str(n) + ') > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li > a > b')  # select_one을 통해 각 제목 얻어와 title에 저장
        price = soup.select_one('#Myform > div:nth-child(' + str(n) + ') > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li > span.ss_p2 > b > span')
        link = soup.select_one('#Myform > div:nth-child(' + str(n) + ') > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li > a.bo3')
        # 저자 찾을 때 li class명이 ss_ht1이 있으면 3번째꺼, 없으면 2번째꺼 크롤링
        html_li = soup.select_one('#Myform > div:nth-child(' + str(n) + ') > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(1) > span.ss_ht1')
        if html_li is None:
            author = soup.select_one('#Myform > div:nth-child(' + str(n) + ') > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2)')
        else:
            author = soup.select_one('#Myform > div:nth-child(' + str(n) + ') > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(3)')

        image = soup.select_one('#Myform > div:nth-child(' + str(n) + ') > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > div > a > img')

        if (title is None or price is None or link is None):
            continue
        if ("크레마" in title.text):
            n += 1
            continue
        else:
            titles.append(title.text)
            prices.append(price.text)
            links.append(link.get('href'))
            authors.append(author.text)
            images.append(image.get('src'))

        n += 1

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
        Book(title=title, bookstore="aladin", weight=value[0],price=value[1], link=value[2], author=value[3], image=value[4], rank=value[5]).save()

    print("알라딘 크롤링 완료")
    #return data
    return True