import pandas as pd, os, time, traceback
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from multiprocessing.pool import ThreadPool
from urllib.parse import urljoin

import tempfile
import json
import pygsheets
import time

debug = True

headers = {"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
           }
domain = "https://delivery.quitanda.com"


def create_driver():
    options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--disable-gpu")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--remote-debugging-port=0")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(service=Service('/home/walter/Documents/Outros/DriverSelenium/chromedriver'), options=options)
    driver.implicitly_wait(7) # wait 7 seconds before raise error
    return driver

XPaths={ #examples
    'Products' : '//*[@id="__next"]/div[2]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div',
    'Name'     : './/div[3]/div/div/div',     
    'Price'    : './/div[4]/div/div/div[1]',  
    'Vol'      : './/div[4]/div/div/div[2]'   
}
driver = create_driver()
driver.get(domain)

# action example
action = webdriver.common.action_chains.ActionChains(driver)
action.click_and_hold(btn).perform()
# sleep for 10 seconds
time.sleep(10)
action.release().perform()