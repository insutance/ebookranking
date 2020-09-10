from selenium import webdriver
import crawling_kyobo, crawling_yes24, crawling_aladin, crawling_naver, crawling_ridibooks
import webdriver

def total_books():
    print("totalbooks 시작")
    driver = webdriver.driver_on()

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

    print("Totalbooks 완료")
    return kyobo_dic, yes24_dic, aladin_dic, naver_dic, ridibooks_dic, total_weight
'''
for key, value in total_weight:
    print(key + ': ' + str(value))
'''


