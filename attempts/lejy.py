import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
# modify the list TABS when there are more tabs
TABS = ["ACT","RULES","REGULATIONS","CIRCULARS","NOTIFICATIONS","GUIDELINES","BY OTHER AUTHORITIES"]
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=3')
driver = webdriver.Chrome("path to chromedriver.exe",chrome_options=options)
# change this path to point to the chromedriver in you system


def find_max_pages(soup):
    print("Finding max pages")
    max_pages= len(soup.find_all("a", {"class": "LinkBL1"}))+1
    return max_pages
# 

def navigate_tabs(url,tabcount,pageno):
    print(url, tabcount,pageno)
    wait_delay = 5
    # this wait delay has to be optimised in an intelligent way.
    # else the total time consumed to run the script will be totalnooftabs*totalnoofpages*5sec which is bad
    driver.set_window_size(1500, 900)
    driver.get(url)
    xpath = '//*[@id="horizontalTab"]/ul/li['+tabcount+']'
    print(xpath)
    # WebDriverWait(driver, wait_delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.find_element_by_xpath(xpath).click()
    # myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))  
    time.sleep(wait_delay)  # you can change this value, by implementing the above line in a nice way, 
    #could not spend much time to get it working, pls check yourself. -Sreekanth
    
    if pageno <2: 
        print("page less than 2")
        soup = parse_page(driver.page_source)
    else:
        print("page more than 2")
        xpath_page = '//*[@id="pagingCont"]/a['+str(pageno-1)+']'
        driver.find_element_by_xpath(xpath_page).click()
        time.sleep(wait_delay)
        soup = parse_page(driver.page_source)
    return soup

def parse_page(htm):
    return BeautifulSoup(htm, "html.parser")

def navigate_pages(soup,max_pages):
    pass


if __name__ == "__main__":
    base_url="https://ibbi.gov.in/webfront/legal_framework.php"
    # change this below for loop when you have more tabs
    for t in range(1,8) :
        tab =str(t)
        print("Parsing data for tab ["+ tab+"]" + TABS[t-1])
        soup_tab=navigate_tabs(base_url,tab,0)
        max_pages = find_max_pages(soup_tab)
        print("Total "+str(max_pages)+" to parse.")
        for p in range(1,max_pages+1):
            print("Parsing data for tab ["+ tab+"] " + TABS[t-1]+" page ["+str(p)+"]")
            soup_page=navigate_tabs(base_url,tab,p)
            data = soup_page.find_all("ul", {"id": "example3"})
            # print("----------------")
            # print(data)
            for i in data:
                lis = i.find_all('a')
                # print(lis)
                for k in lis:
                    # print(k)
                    if re.match('javascript:newwindow1',k['onclick']):
                        pdf_url= k['onclick'].replace("javascript:newwindow1(","").replace(");","")
                        if "http" in pdf_url:
                            print (i.text,pdf_url)
                            # this is the data you need, you can disable all other prints and print only this
                            # or rather you could also write this into a file


