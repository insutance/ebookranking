import os
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from index.models import Book

def crawling_init():
    print("**********네이버 크롤링 시작**********")
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    #driver = webdriver.Chrome('/Users/insutance/Downloads/chromedriver',options=chrome_options)  # options는 우리가 추가한 옵션 추가해주기 위해 넣음
    
    print('naver website start!!')
    driver.get('https://series.naver.com/ebook/top100List.nhn')
    driver.implicitly_wait(2)  # 버퍼때문에 2초간 기다리게 함
    html1 = driver.page_source

    button = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div[2]/a[1]')
    button[0].click()  # 버튼 클릭
    driver.implicitly_wait(2)  # 버퍼때문에 2초간 기다리게 함
    html2 = driver.page_source

    soup1 = BeautifulSoup(html1, 'html.parser')
    soup2 = BeautifulSoup(html2, 'html.parser')
    
    driver.quit()
    return soup1, soup2

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
'''
Main Code
'''
def naver():
    soup1, soup2 = crawling_init()
    print('init finish!')
    
    titles = []     # 제목 저장 리스트
    prices = []     # 가격 저장 리스트
    links = []      # 링크 저장 리스트
    authors = []    # 저자 저장 리스트
    images = []     # 이미지 저장 리스트

    n = 1
    while(n < 5):
        m = 1
        while(m < 6):
            title = soup1.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > a > strong')
            price = soup1.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > p > strong > span')
            link = soup1.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > a')
            author = soup1.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > a > span.writer')
            image = soup1.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > a > img')

            if (title is None or price is None or link is None):
                continue
            else:
                titles.append(title.text)
                prices.append(price.text)
                links.append("https://series.naver.com" + link.get('href'))
                authors.append(author.text)
                images.append(image.get('src'))

            m += 1
        n += 1

    n = 1
    while(n < 3):
        m = 1
        while(m < 6):
            title = soup2.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > a > strong')
            price = soup2.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > p > strong > span')
            link = soup2.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > a')
            author = soup2.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > a > span.writer')
            image = soup2.select_one('#content > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > a > img')

            if (title is None or price is None or link is None):
                continue
            else:
                titles.append(title.text)
                prices.append(price.text)
                links.append("https://series.naver.com" + link.get('href'))
                authors.append(author.text)
                images.append(image.get('src'))

            m += 1
        n += 1

    titles = clearTitle(titles)
    prices = clearPrice(prices)

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
        Book(title=title, bookstore="naver", weight=value[0],price=value[1], link=value[2], author=value[3], image=value[4], rank=value[5]).save()

    print("**********네이버 크롤링 완료**********")
    #return data
    return True