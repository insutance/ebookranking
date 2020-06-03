import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebookranking.settings')    # Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
django.setup()  # 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
from index.models import Kyobo,Yes24,Aladin,Naver,Ridibooks,TotalBooks   #이거 순서때문에 계속 오류 나던거였냐 .. ?
import crawling_totalbooks

def delete_data():
    Kyobo.objects.all().delete()
    Yes24.objects.all().delete()
    Aladin.objects.all().delete()
    Naver.objects.all().delete()
    Ridibooks.objects.all().delete()
    TotalBooks.objects.all().delete()

def insert_data():
    kyobo_dic, yes24_dic, aladin_dic, naver_dic, ridibooks_dic, totalbooks_dic = crawling_totalbooks.total_books()

    for title,value in kyobo_dic.items():
        Kyobo(title=title, price=value[1], link=value[2], author=value[3], image=value[4]).save()

    for title,value in yes24_dic.items():
        Yes24(title=title, price=value[1], link=value[2], author=value[3], image=value[4]).save()

    for title,value in aladin_dic.items():
        Aladin(title=title, price=value[1], link=value[2], author=value[3], image=value[4]).save()

    for title,value in naver_dic.items():
        Naver(title=title, price=value[1], link=value[2], author=value[3], image=value[4]).save()

    for title,value in ridibooks_dic.items():
        Ridibooks(title=title, price=value[1], link=value[2], author=value[3], image=value[4]).save()

    for title, weight in totalbooks_dic:
        TotalBooks(title=title, weight=weight).save()

if __name__=='__main__':
    delete_data()
    insert_data()
    


