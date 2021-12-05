# 쿠팡 스크랩핑

import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
res = requests.get(url, headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items=soup.find_all("li", attrs = {"class":"search-product"})
print(items)


# search-product로 시작하는 모든 클래스중에서 li태그인 것들만 구하기
# items = soup.find_all("a",attrs ={"class":"^search-product"})
# print(items.a.get_text())

# for item in items:
#     # 제품명
#     name = item.find("div", attrs={"class":"name"}).get_text()

#     # 가격
#     price = item.find("strong", attrs={"class":"price-value"}).get_text()

#     # 평점
#     rate = item.find("em", attrs={"class":"rating"})
#     if rate:
#         rate = rate.get_text()
#     else:
#         rate = "평점 없음"

#     # 평점 수 
#     rate_cnt = item.find("span", attrs={"class":"rating-total-count"}).get_text()

#     print(name)
#     print(price)
    