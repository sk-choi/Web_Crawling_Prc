#selenium 4 버전 이상부터는 chrome driver를 따로 설치하지 않아도 된다. 

# import os
# os.system('pip install --upgrade selenium') #selenium 최신 버전 자동 설치

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(3) #페이지 로딩이 완료될 때까지 기다리는 코드 : 3초

driver.get("https://google.com") #사이트 접속하기

#요소찾기

#class name으로 찾기
driver.find_element(By.CLASS_NAME,'gLFyf')

#tag name으로 찾기
driver.find_element(By.TAG_NAME,'textarea')

#id로 찾기
driver.find_element(By.ID,'APjFqb')

#Xpath로 찾기
driver.find_element(By.XPATH,'//*[@id="APjFqb"]')


#요소 활용하기

#클릭하기
driver.find_element(By.XPATH,'//*[@id="APjFqb"]').click()

#값 입력하기
driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys("tistory")

#키보드 입력하기
driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys(Keys.ENTER)

#티스토리 링크 클릭
driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()