import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/mysterymachine/Desktop/Assignment_3/chromedriver')
base_url = "http://www.whosdatedwho.com/popular?letter="
# query = <alphabets from a to z>
browser.get(base_url + query)

time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 3000

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_xpath("//a[@href]")

for post in post_elems:
    print post.get_attribute("href")
