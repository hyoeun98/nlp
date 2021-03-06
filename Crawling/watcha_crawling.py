import selenium
import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

def crawl(i):
    time.sleep(1)
    try:
        movie_title = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[2]/div/div/div[3]/h1')
    except: # 제목이 img
        movie_title = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[2]/div/div/div[3]/img').get_attribute('alt')
    else: # 제목이 h1
        movie_title = movie_title.text
        
    try:
        moive_type = driver.find_element_by_class_name(f'closed')
    except: # 영화
        movie_info = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[2]/div/div/div[3]/div[2]/div[2]')
        movie_rating = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[2]/div/div/div[3]/div[1]/div[1]/div[2]/div[2]')
    else: # 시즌이 여러개인 드라마
        movie_info = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[2]/div/div/div[3]/div[3]/div[2]')
        movie_rating = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[2]/div/div/div[3]/div[2]/div[1]/div[2]/div[2]')

#     print(movie_title)
#     print(movie_info.text)
#     print(movie_rating.text)
    data = {'title':movie_title,
          'story':movie_info.text,
          'rating':movie_rating.text}
    return data


URL = 'https://watcha.com/sign_in'
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome(options=options, executable_path='C:/anaconda/chromedriver')
driver.implicitly_wait(time_to_wait=5)
driver.get(url=URL)

driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/div[1]/main/div/form/div[1]/input').send_keys('id@naver.com')
driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/div[1]/main/div/form/div[2]/input').send_keys('pw')
driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/div[1]/main/div/form/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="root"]/div[1]/main/div[1]/section/ul/li[4]/button/div[2]').click()
driver.find_element_by_xpath('//*[@id="root"]/div[1]/nav/ul[2]/li[2]/div/div/div/a').click() # 프로필 선택

df = pd.DataFrame(columns=['title', 'story', 'rating'])

for i in range(1,5):
    movie = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[1]/ul/li[1]/div/div[1]/div[1]/div[2]')
    ActionChains(driver).move_to_element(movie).pause(1.5).perform()
    hidden_button = driver.find_element_by_class_name('css-g373u1-StyledEmbedButton')
    hidden_button.click()
    df = df.append(crawl(i),ignore_index=True)
    
    movie = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[1]/ul/li[2]/div/div[1]/div[1]/div[2]')
    movie.click()
    df = df.append(crawl(i),ignore_index=True)
    
    movie = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[1]/ul/li[3]/div/div[1]/div[1]/div[2]')
    movie.click()
    df = df.append(crawl(i),ignore_index=True)
    
    movie = driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[1]/ul/li[4]/div/div[1]/div[1]/div[2]')
    movie.click()
    df = df.append(crawl(i),ignore_index=True)

    driver.find_element_by_xpath(f'//*[@id="root"]/div[1]/main/div[1]/section/ul/li[{i}]/div[2]/div/div/div[2]').click()
    time.sleep(1)
    driver.find_element_by_tag_name('body').send_keys('Keys.PAGE_DOWN')


print(df)



