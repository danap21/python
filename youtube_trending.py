import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

PATH = "C:\Program Files (x86)\chromedrive.exe" #Path of Chrome Driver
driver = webdriver.Chrome(PATH)


driver.get("https://youtube.com")
print(driver.title + '\n') #print title

driver.implicitly_wait(10) #wait for webpage to load for a few secs

#Navigate to Trending
menu_button = driver.find_element(By.XPATH, "//*[@id='guide-icon']")
menu_button.click()

time.sleep(3)

trending_button = driver.find_element(By.XPATH, "//*[@title='Trending']")
trending_button.click()

driver.refresh()
ActionChains(driver)\
    .send_keys(Keys.END)\
    .perform()

time.sleep(3)

#Grab Trending Titles
#trending_titles = driver.find_elements(By.XPATH, "//*[@id='video-title']")

videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-video-renderer')

videoList = []

for video in videos:
    #Added .// for search withint the element and not the whole page
    titles = video.find_element(By.XPATH, ".//*[@id='video-title']/yt-formatted-string")
    view_count =  video.find_element(By.XPATH, ".//*[@id='metadata-line']/span[1]")
    date = video.find_element(By.XPATH, ".//*[@id='metadata-line']/span[2]")
    print(titles.text + " | " + view_count.text + " | " + date.text)

    vidList = {
        'Title': titles,
        'Views': view_count,
        'Date': date
    }
    
    videoList.append(vidList)

df = pd.DataFrame(videoList)
print(df)

time.sleep(5)


