import requests
from bs4 import BeautifulSoup

# url = "https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
url = "https://www.tradlinx.com/tracking"

response = requests.get(url)

if response.status_code == 200:
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  # title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')  
  # print(title)
  title = soup.select_one('body > application > div > container-tracking > div > div.common-title-layer > h1 > p')
  print(title)
  
  # titles = ul.select('li > dl > dt > a')
  # for title in titles:
  #   print(title.get_text())

else :
  print(response.status_code)

