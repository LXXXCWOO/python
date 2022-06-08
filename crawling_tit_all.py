from urllib.request import urlopen
from bs4 import BeautifulSoup

# 뉴스기사 검색 URL
url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

# urlopen 함수를 통해 url주소를 open하여 읽고, 그 값을 html 이라는 변수에 저장합니다.
html = urlopen(url).read()

# html 정보가 담겨있는 변수를 bs4 라이브러리에 있는 BeautifulSoup를 이용해
# html 정보를 parsing 하여 soup 에 저장합니다.
soup = BeautifulSoup(html, 'html.parser')

# 제목 전체를 검색한다.
html_class = soup.find_all(class_='news_tit')

# 뉴스제목을 Text로 추출하여 출력합니다.
for tit in html_class:
    title = tit.text.strip()
    print(title)
