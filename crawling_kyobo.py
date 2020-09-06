from bs4 import BeautifulSoup
from selenium import webdriver
import re

def crawling_init(driver):
    print("교보문고 크롤링 시작")

    driver.get('http://m.kyobobook.co.kr/digital/ebook/bestList.ink?cate_code=1&class_code=&barcode=&barcodes=&cate_gubun=&orderClick=&listCateGubun=1&listSortType=1&listSortType2=0&listSortType3=0&listSortType4=0&need_login=N&type=&returnUrl=%2Fdigital%2Febook%2FbestList.ink&reviewLimit=0&refererUrl=&barcodes_temp=&gubun=&ser_product_yn=&groupSort=1&groupSort2=0&groupSort3=0&groupSort4=0')
    driver.implicitly_wait(2)  # 버퍼때문에 2초간 기다리게 함

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 교보문고 사이트에서 링크따오기
    driver.get('http://digital.kyobobook.co.kr/digital/publicview/publicViewBest.ink?tabType=EBOOK&tabSrnb=12')
    driver.implicitly_wait(2)  # 버퍼때문에 2초간 기다리게 함
    button = driver.find_elements_by_xpath('//*[@id="selectDateType"]/option[2]')   #주간 클릭
    button[0].click()  # 버튼 클릭

    webhtml1 = driver.page_source
    soupweb1 = BeautifulSoup(webhtml1, 'html.parser')

    button = driver.find_elements_by_xpath('//*[@id="neo_conbody"]/div/div[3]/a[3]') #//*[@id="neo_conbody"]/div[2]/a[3] 에서 변경
    button[0].click()
    
    webhtml2 = driver.page_source
    soupweb2 = BeautifulSoup(webhtml2, 'html.parser')

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
def kyobo(driver):
    soup, soupweb1, soupweb2 = crawling_init(driver)

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
    for n in range(len(titles)):
        title_data = []
        title_data.append(round(weight * 0.25, 2))
        title_data.append(prices[n])
        title_data.append(links[n])
        title_data.append(authors[n])
        title_data.append(images[n])
        data[titles[n]] = title_data
        weight -= 1

    print("교보문고 크롤링 완료")
    return data

