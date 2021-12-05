import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") 

# 만화 목록 모두 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"}) # 태그명이 a이고 클래스가 title인 모든 값들

for cartoon in cartoons:
    print(cartoon.get_text())