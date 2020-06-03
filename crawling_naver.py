from bs4 import BeautifulSoup
from selenium import webdriver
import re

def crawling_init():
    options = webdriver.ChromeOptions()  # option 생성
    options.add_argument('headless')  # 창 안띄우게 하는 옵션 추가
    options.add_argument("--disable-gpu")  # gpu 사용 안 한다는거
    options.add_argument("lang=ko_KR")  # 한국어로 설정
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")  # UserAgent 탐지를 막기 위해

    driver = webdriver.Chrome('C:\\Users\\insutance\\PycharmProjects\\chromedriver',options=options)  # options는 우리가 추가한 옵션 추가해주기 위해 넣음
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
    for n in range(len(titles)):
        title_data = []
        title_data.append(round(weight * 0.15, 2))
        title_data.append(prices[n])
        title_data.append(links[n])
        title_data.append(authors[n])
        title_data.append(images[n])
        data[titles[n]] = title_data
        weight -= 1

    return data