import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas as pd
import csv
import time

browser = webdriver.Chrome('/Users/mysterymachine/Desktop/Assignment_3/chromedriver')

browser.get("https://empeopled.com")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 5

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    no_of_pagedowns-=1


titles=[]
usernames=[]
votes=[]
dates=[]
tags=[]


title_elements = browser.find_elements_by_xpath("//*[@class=\"post\"]/div/div[2]/div/div[2]/a[1]")
for element in title_elements:
    print element.text

username_elements = browser.find_elements_by_xpath("//*[@class=\"post\"]/div/div[2]/div/div[2]/p[1]/a")
for element in username_elements:
    usernames.append(element.text)

vote_elements = browser.find_elements_by_xpath("//*[@class=\"post\"]/div/div[2]/div/div[2]/p[2]/span[1]/span/span")
for element in vote_elements:
    votes.append(element.text)

date_elements = browser.find_elements_by_xpath("//*[@class=\"post\"]/div/div[2]/div/div[2]/p[1]/span[2]")
for element in date_elements:
    dates.append(element.text)

tag_elements = browser.find_elements_by_xpath("//*[@class=\"post\"]/div/div[2]/div/div[2]/p[1]/span[1]/a")
for element in tag_elements:
    tags.append(element.text)

df = pd.DataFrame(titles, columns=['Title'])
df['Username']=pd.Series(usernames)
df['Vote_Count']=pd.Series(votes)
df['Date']=pd.Series(dates)
df['Tags']=pd.Series(tags)

filename = '/Users/mysterymachine/Desktop/Assignment_3/empeopled.csv'

with open(filename, 'a') as f:
    df.to_csv(filename, index=False, encoding='utf-8')
    print "done"
