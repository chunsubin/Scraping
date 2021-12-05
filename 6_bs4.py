import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

# html문서값을 lxml파서를 통해 soup객체를 만드는 작업
soup = BeautifulSoup(res.text, "lxml") 
# print(soup.title)  # <title>네이버 만화</title>
# print(soup.title.get_text())  # 네이버 만화 (태그가 제거됨)

# print(soup.a)  # soup 객체에서 처음 나타나는 a태그의 내용
# print(soup.a.attrs)  # a element의 속성 정보를 출력

# print(soup.a["href"]) # a원소의 href 속성값  --> #menu 출력

## <a href="/mypage/myActivity" class="Nbtn_upload" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
# 위아 같은 태그에 대한 내용을 출력하고 싶을때 find함수 이용
tmp = soup.find("a", attrs={"class":"Nbtn_upload"})  # 클래스 이름이 Nbtn-이고 a태그인 것을 찾아줘
tmp = soup.find(attrs={"class":"Nbtn_upload"})  # class이름이 nbtn인 어떠한 태그를 찾아줘


# 실시간 웹툰 1등인 것을 출력해보기
# tmp = soup.find("li", attrs={"class":"rank01"})
# print(tmp.a)  # rank01클래스의 a태그 내용 출력


# 실시간 웹툰 1등, 2등, 3등 .. 차례로 정보 추출
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())  # 태그 제외 하고 출력됨 (외모지상주의-368화 원나잇lll [09])

rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling 

print(rank2.a.get_text()) # 나 혼자 만렙 뉴비-19화. 
print(rank3.a.get_text()) # 검성 천유성 재혼 황후-90화

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text()) # next 반대 명령어는 previous

# print(rank1.parent)
print()
tmp = rank1.find_next_sibling("li") # li 리스트 태그에 해당하는 것들만 출력
print(tmp.a.get_text())

print("-----------------------")
print(rank1.find_next_siblings("li"))
