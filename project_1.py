import requests
from bs4 import BeautifulSoup


def create_soup(url):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    res = requests.get(url, headers=header)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%98%B8%EC%9B%90%EB%8F%99%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hjoIdwp0YidssLEyuSdssssssSw-369936"

    soup = create_soup(url)

    print("[* 오늘의 호원동 날씨 *]")

    # 오늘 날씨  # 어제보다 5도낮아요 / 맑음
    cast = soup.find("p", attrs = {"class":"summary"})
    summary_text = cast.get_text()
    
    # 현재 온도
    curr_temp = soup.find("div", attrs = {"class":"temperature_text"}).get_text()[1:]

    # 최저 기온, 최고 기온
    min_temp = soup.find("span", attrs = {"class":"lowest"}).get_text()
    max_temp = soup.find("span", attrs = {"class":"highest"}).get_text()

    # 강수 확률
    weather_left = soup.find("span", attrs = {"class":"weather_left"})
    morning_rain_rate = weather_left.span.get_text()
    afternoon_rain_rate = weather_left.span.next_element.get_text()

    # 미세먼지
    dust = soup.find("ul", attrs = {"class":"today_chart_list"})
    pm10 = dust.find_all("li")[0].get_text()
    pm25 = dust.find_all("li")[1].get_text()
    uv = dust.find_all("li")[2].get_text()

    #출력
    print(summary_text[:11]+"/"+summary_text[12:]) 
    print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
    print("강수 : 오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print(pm10[2:])
    print(pm25[2:])
    print(uv[2:])

def scrape_headline_news():
    url = "https://news.naver.com"
    print("[ 오늘의 헤드라인 뉴스]")
    soup = create_soup(url)
    news_list = soup.find("ul", {"class":"hdline_article_list"}).find_all("li")
    for idx, news in enumerate(news_list):
       headline = news.find("div", {"class":"hdline_article_tit"}).a.get_text()
       headline=headline.strip()
       link = url + news.find("a")["href"]
       print("{}. {}".format(idx + 1, headline))
       print("링크 : {}".format(link))



if __name__ == "__main__":
    #scrape_weather()  # 오늘의 날씨 정보 가져오기
    scrape_headline_news()