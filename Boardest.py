import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas as pd
import csv
import time

browser = webdriver.Chrome('/Users/mysterymachine/Desktop/Assignment_3/chromedriver')

browser.get("http://en.boardest.com/")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 1250

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    no_of_pagedowns-=1


titles=[]
usernames=[]
stories=[]
dates=[]
tags=[]

title_elements = browser.find_elements_by_xpath("//*[@class=\"scope-thread story story-unit\"]/article/div[1]/div[2]/h2")

for element in title_elements:
    titles.append(element.text)

username_elements = browser.find_elements_by_xpath("//*[@class=\"scope-thread story story-unit\"]/article/div[1]/div[2]/div[2]/div[2]/span")

for element in username_elements:
    usernames.append(element.text)

story_elements = browser.find_elements_by_xpath("//*[@class=\"scope-thread story story-unit\"]/article/div[2]/div")

for element in story_elements:
    stories.append(element.text)

date_elements = browser.find_elements_by_xpath("//*[@class=\"scope-thread story story-unit\"]/article/div[1]/div[2]/div[1]/span[5]")

for element in date_elements:
    dates.append(element.text)

tag_elements = browser.find_elements_by_xpath("//*[@class=\"scope-thread story story-unit\"]/article/div[1]/div[2]/div[1]/span[3]/span")

for element in tag_elements:
    tags.append(element.text)

df = pd.DataFrame(titles, columns=['Title'])
df['Username']=pd.Series(usernames)
df['Story']=pd.Series(stories)
df['Date']=pd.Series(dates)
df['Tags']=pd.Series(tags)

filename = '/Users/mysterymachine/Desktop/Assignment_3/boardest_1000.csv'

with open(filename, 'a') as f:
    df.to_csv(filename, index=False, encoding='utf-8')
    print "done"
