import requests
res=requests.get("http://naver.com")
res=requests.get("http://ccssbb.tistory.com")
res.raise_for_status()  # 이상하면 오류발생시키기
print(res.status_code)

# if res.status_code == requests.codes.ok:  # 상태코드가 200이면
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다")

print(len(res.text))

with open("mygoogle.html","w",encoding="utf8") as f:  # mygoogle 파일 생성된다.
    f.write(res.text)