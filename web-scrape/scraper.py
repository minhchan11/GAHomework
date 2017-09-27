import platform
import requests
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

if platform.system() == "Windows":
    PHANTOMJS_PATH = './phantomjs.exe'
else:
    PHANTOMJS_PATH = '/usr/local/bin/phantomjs'

browser = webdriver.PhantomJS(PHANTOMJS_PATH)
browser.get('http://www.scoreboard.com/en/tennis/atp-singles/us-open-2015/results/')

# let's parse our html
soup = BeautifulSoup(browser.page_source, "html.parser")
# print(soup)
# get all the games
games = soup.find_all(name='tr', attrs={'class': 'stage-finished'})

# and print out the html for first game
if games:
    print(games[0].prettify())
