import cgi
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from os import environ
import time
import urllib
from urllib.request import urlopen
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import ssl
import urllib3

form = cgi.FieldStorage



driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(0.5)
driver.get('https://www.ups.com/track?loc=en_US&requester=ST/')

trackingnumber = form.getvalue("trackingnumber")
carrier = form.getvalue("carrier")

inputElement = driver.find_element_by_id("stApp_trackingNumber")
inputElement.send_keys('1')
