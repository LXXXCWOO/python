from urllib.request import urlopen
from bs4 import BeautifulSoup

# 뉴스기사 검색 URL
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=sue+over&tqi=hFzanwprvTVss7Ye7YwssssssLo-392202"

# urlopen 함수를 통해 url주소를 open하여 읽고, 그 값을 html 이라는 변수에 저장합니다.
html = urlopen(url).read()

# html 정보가 담겨있는 변수를 bs4 라이브러리에 있는 BeautifulSoup를 이용해
# html 정보를 parsing 하여 soup 에 저장합니다.
soup = BeautifulSoup(html, 'html.parser')

# 검색페이지 첫번째 타이틀 값을 반환, 표시
title = soup.find(class_='title')
temperature = soup.find(class_='temperature_text')
weather = soup.find(class_='weather before_slash')

# 데이터 출력
print(title.text)
print(temperature.text)
print(weather.text)
