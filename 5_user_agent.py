import requests
url = "http://ccssbb.tistory.com"
# 나의 에이전트
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
res=requests.get(url, headers=headers) # 페이지 접속할때 user agent를 넘겨준다
res.raise_for_status()  # 이상하면 오류발생시키기

with open("ccssbb.html","w",encoding="utf8") as f:  # mygoogle 파일 생성된다.
    f.write(res.text)