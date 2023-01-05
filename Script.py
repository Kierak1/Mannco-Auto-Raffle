from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from parsel import Selector
from random import choice
import undetected_chromedriver as uc
import time
import pickle
import pprint
import re
import random
import requests
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("ok")

def collection():
    try:
        chrome.get("https://mannco.store/giveaways")
        time.sleep(2)
        links = [link.get_attribute("href") for link in chrome.find_elements_by_xpath("//div[@class='raffle-list list-group rfl']/a[@href]")]
        print("shitted1")
        for link in links:
         try: 
             chrome.get(link)
         except: 
             print("Links pooped")
             chrome.quit()
         try:
             WebDriverWait(chrome, 2).until(EC.element_to_be_clickable((By.XPATH,"(//a[contains(.,'Join Now')])[last()]"))).click()
             print("Button found and pressed")
             #sleep(randint(4,5))
         except:
             #sleep(randint(0,1))
             print("Button not found but the script is still running")
    except:
        print("shitted")

createFolder('C:\\Mannco\\')
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Mannco")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")  
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('disable-infobars')
options.add_argument('--window-size=1024,768')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
chrome = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\chromedriver', chrome_options=options)

#chrome.get("https://mannco.store/")
#time.sleep(70)
collection()
chrome.quit()