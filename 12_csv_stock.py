import csv
import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

for page in range(1,2):
    res = requests.get(url + str(page), headers = header)
    res.raise_for_status()
    soup = BeautifulSoup(res, "lxml")

    # table태그 , 클래스명 : type_2 , 종속된 tbody , tbody에 종속된 tr태그
    data_rows = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all({"tr"})  
    for row in data_rows:
        columns = row.find_all("td")
        data = [column.get_text() for column in columns]
        print(data)

