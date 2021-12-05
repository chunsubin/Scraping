# webdriver 창이 켜졌다가 아무런 작업도 하지않았음에도 바로 꺼지는 현상
# 해결하지 못함


from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('chromedriver.exe', options=options)