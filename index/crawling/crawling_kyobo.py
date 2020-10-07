import os
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from index.models import Book
from django.utils import timezone
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def crawling_init():
    print("교보문고 크롤링 시작")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    #driver = webdriver.Chrome('/Users/insutance/Downloads/chromedriver',options=chrome_options)  # options는 우리가 추가한 옵션 추가해주기 위해 넣음
    print("mobile start")
    driver.get('http://m.kyobobook.co.kr/digital/ebook/bestList.ink?cate_code=1&class_code=&barcode=&barcodes=&cate_gubun=&orderClick=&listCateGubun=1&listSortType=1&listSortType2=0&listSortType3=0&listSortType4=0&need_login=N&type=&returnUrl=%2Fdigital%2Febook%2FbestList.ink&reviewLimit=0&refererUrl=&barcodes_temp=&gubun=&ser_product_yn=&groupSort=1&groupSort2=0&groupSort3=0&groupSort4=0')
    driver.implicitly_wait(2)  # 버퍼때문에 2초간 기다리게 함

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print("website start")
    # 교보문고 사이트에서 링크따오기
    driver.get('http://digital.kyobobook.co.kr/digital/publicview/publicViewBest.ink?tabType=EBOOK&tabSrnb=12')
    try:
        element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="selectDateType"]/option[2]'))
            )
    except TimeoutException:
        return False
    button = driver.find_elements_by_xpath('//*[@id="selectDateType"]/option[2]')   #주간 클릭
    button[0].click()  # 버튼 클릭

    webhtml1 = driver.page_source
    soupweb1 = BeautifulSoup(webhtml1, 'html.parser')

    try:
        element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="neo_conbody"]/div/div[3]/a[3]'))
            )
    except TimeoutException:
        return False
    button = driver.find_elements_by_xpath('//*[@id="neo_conbody"]/div/div[3]/a[3]') #//*[@id="neo_conbody"]/div[2]/a[3] 에서 변경
    button[0].click()
    
    webhtml2 = driver.page_source
    soupweb2 = BeautifulSoup(webhtml2, 'html.parser')
    
    driver.quit()
    print("driver quit")
    return soup, soupweb1, soupweb2

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
def kyobo():
    soup, soupweb1, soupweb2 = crawling_init()
    print("init finish")
    titles = []     # 제목 저장 리스트
    prices = []     # 가격 저장 리스트
    links = []      # 링크 저장 리스트
    authors = []    # 저자 저장 리스트
    images = []     # 이미지 저장 리스트

    n = 1
    while(len(titles) < 30):
        title = soup.select_one('#list > li:nth-child(' + str(n) + ') > div.detail > p.pubTitle > a')  # select_one을 통해 각 제목 얻어와 title에 저장
        price = soup.select_one('#list > li:nth-child(' + str(n) + ') > div.detail > p.pubPrice > span > strong')
        image = soup.select_one('#list > li:nth-child(' + str(n) + ') > div.pic_area > a > img')
        
        if(title is None or price is None):
            continue
        else:
            titles.append(title.text)
            prices.append(price.text)
            images.append(image.get('src'))

        n += 1

    titles = clearTitle(titles)
    prices = clearPrice(prices)

    for n in range(1, 6):
        link = soupweb1.select_one('#listContent > div > ul.best5 > li:nth-child(' + str(n) + ') > div.pic_area > a')
        author = soupweb1.select_one('#listContent > div > ul.best5 > li:nth-child(' + str(n) + ') > div.cont_area > div.info1 > span.n1')

        links.append("http://digital.kyobobook.co.kr" + link.get('href'))
        authors.append(author.text)

    for n in range(2, 5):
        for m in range(1, 6):
            link = soupweb1.select_one('#listContent > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > div.pic_area > a')
            author = soupweb1.select_one('#listContent > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > div.cont_area > div.info1 > span.n1')

            links.append("http://digital.kyobobook.co.kr" + link.get('href'))
            authors.append(author.text)

    for n in range(1, 3):
        for m in range(1, 6):
            link = soupweb2.select_one('#listContent > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > div.pic_area > a')
            author = soupweb2.select_one('#listContent > div > ul:nth-child(' + str(n) + ') > li:nth-child(' + str(m) + ') > div.cont_area > div.info1 > span.n1')

            links.append("http://digital.kyobobook.co.kr" + link.get('href'))
            authors.append(author.text)

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
        Book(title=title, bookstore="kyobo", weight=value[0], price=value[1], link=value[2], author=value[3], image=value[4], rank=value[5]).save()

    print("교보문고 크롤링 완료")
    #return data
    return True