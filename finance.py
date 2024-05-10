import os
import pandas as pd               # 웹페이지에서 테이블 부분만의 데이터를 읽어올수 있음
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()    
# browser = webdriver.Chrome()
browser = webdriver.Edge()
browser.maximize_window()

# 1. 페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

# 2. 조회 항목 초기화 (기존 체크되어 있는 항목 해제)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected():
       checkbox.click()

# 3. 조회 항목 설정 (내가 원하는 항목으로 체크)
items_to_select = ['거래량', '매수호가', '매도호가']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..')
    label = parent.find_element(By.TAG_NAME, 'label')
    #print(label.text)
    if label.text in items_to_select:
       checkbox.click() 

# 4. 적용하기 click
btn_apply = browser.find_element(By.XPATH, '//a[@href = "javascript:fieldSubmit()"]')  
btn_apply.click()

for idx in range(1,3):
    browser.get(url + str(idx))
    # 5. 데이터 추출
    df = pd.read_html(browser.page_source)[1]
    print(df)
    print("################################################################")
    df.dropna(axis='index', how='all', inplace=True)
    print(df)
    print("################################################################")
    df.dropna(axis='columns', how='all', inplace=True)
    print(df)
    print("################################################################")
    # 6. 파일 지정
    f_name = 'sisa.csv'
    if os.path.exists(f_name):
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else:
        df.to_csv(f_name, encoding='utf-8-sig', index=False)   #mode는 default가 write 임  a->append

    print(f'{idx} 페이지 완료')

# browser.quit()   #프로그램이 결과 값 출력 후 브라우져를 닫지 않도록 임시로 disable 함

