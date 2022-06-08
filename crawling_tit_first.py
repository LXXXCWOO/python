from urllib.request import urlopen
from bs4 import BeautifulSoup

# 뉴스기사 검색 URL
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
url2 = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%9E%90%EC%A0%84%EA%B1%B0"

# urlopen 함수를 통해 url주소를 open하여 읽고, 그 값을 html 이라는 변수에 저장합니다.
html = urlopen(url).read()
html2 = urlopen(url2).read()

# html 정보가 담겨있는 변수를 bs4 라이브러리에 있는 BeautifulSoup를 이용해
# html 정보를 parsing 하여 soup 에 저장합니다.
soup = BeautifulSoup(html, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')

# 검색페이지 첫번째 타이틀 값을 반환, 표시
first_found = soup.find(class_='news_tit')
print(first_found.text)

second_found = soup2.find(class_='news_tit')
print(second_found.text)
