import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=335885'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 1) 가우스 웹툰 제목 출력
# cartoons = soup.find_all("td",attrs={"class":"title"})
# title=cartoons[0].a.get_text()
# link = cartoons[0].a["href"] # 링크태그인 href의 내용을 가져온다
# print(title)
# print("https://comic.naver.com" + link)


# 2) 가우스 제목과 해당 만화 링크 같이 구하기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)


# 3) 평점 구하기
total_ranks = 0
cartoons = soup.find_all("div",attrs={"class":"rating_type"})
for cartoon in cartoons:
    rank = cartoon.strong.get_text()
    print(rank)
    total_ranks += float(rank)

print("전체 평점은 ", total_ranks)
print("평균 점수는 ", total_ranks/len(cartoons))