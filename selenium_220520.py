import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url='https://www.google.com')
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'Fgvgjc'))
    )
finally:
    driver.quit()

# # 현재 url 얻기
# print(driver.current_url)

# # 브라우저 닫기
# driver.close()
