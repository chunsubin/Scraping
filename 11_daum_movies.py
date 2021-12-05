# 다음에 '영화 순위'를 쳐서 순위권 영화의 포스터 사진을 가져오기
# 큰 사진을 가져오기 위해서 똑같은 포스터 사진을 세번 눌러야 한다.
# 따라서, 이미지 링크를 가져와서 클릭을 세 번 하는 작업을 해야함

import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class":"thumb_img"})

# 1~5등 까지인 영화들의 이미지가 다운받아짐
# for idx, image in enumerate(images):
#     image_url = image["src"]
#     if image_url.startswith("//"):   # //로 시작한다면 앞쪽에 http:붙여주기
#         image_url +="http:"
    
#     print(image_url)
#     image_res = requests.get(image_url)
#     image_res.raise_for_status()

#     with open("movie{}.jpg".format(idx+1), "wb") as f:  # 바이너리 데이터
#         f.write(image_res.content)  # content는 이미지

#     if idx>=4: break


# 2015~2021년까지 연도별로 상위5위 영화 정보
for year in range(2015,2021):
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):   # //로 시작한다면 앞쪽에 http:붙여주기
            image_url +="http:"
        
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie{}_{}.jpg".format(year,idx+1), "wb") as f:  # 바이너리 데이터
            f.write(image_res.content)  # content는 이미지

        if idx>=4: break