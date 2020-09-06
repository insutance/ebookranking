from bs4 import BeautifulSoup
from selenium import webdriver
import re

def crawling_init(driver):
    print("알라딘 크롤링 시작")
    '''
    options = webdriver.ChromeOptions()  # option 생성
    options.add_argument('headless')  # 창 안띄우게 하는 옵션 추가
    options.add_argument("--disable-gpu")  # gpu 사용 안 한다는거
    options.add_argument("lang=ko_KR")  # 한국어로 설정
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")  # UserAgent 탐지를 막기 위해

    driver = webdriver.Chrome('/Users/insutance/Downloads/chromedriver',options=options)  # options는 우리가 추가한 옵션 추가해주기 위해 넣음
    '''
    # driver = webdriver.Chrome('C:\\Users\\insutance\\PycharmProjects\\chromedriver')
    driver.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=9&BestType=EBookBestseller')
    driver.implicitly_wait(2)  # 버퍼때문에 2초간 기다리게 함

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #driver.quit()

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
def aladin(driver):
    soup = crawling_init(driver)

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
    for n in range(len(titles)):
        title_data = []
        title_data.append(round(weight * 0.25, 2))
        title_data.append(prices[n])
        title_data.append(links[n])
        title_data.append(authors[n])
        title_data.append(images[n])
        data[titles[n]] = title_data
        weight -= 1

    print("알라딘 크롤링 완료")
    return data