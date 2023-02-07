import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedrive.exe" #Path of Chrome Driver
driver = webdriver.Chrome(PATH)


driver.get("https://youtube.com")
print(driver.title + '\n') #print title

driver.implicitly_wait(10) #wait for webpage to load for a few secs

#Navigate to Trending
menu_button = driver.find_element(By.XPATH, "//*[@id='guide-icon']")
menu_button.click()

time.sleep(5)

trending_button = driver.find_element(By.XPATH, "//*[@title='Trending']")
trending_button.click()

driver.refresh()

#Grab Trending Titles
trending_titles = driver.find_elements(By.XPATH, "//*[@id='video-title']")

for i in trending_titles:
    print(i + i.text + "\n")

driver.implicitly_wait(20)

time.sleep(5)

