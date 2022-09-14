#Examples of UPS and USPS tracking delivered successfully
#
#https://wwwapps.ups.com/WebTracking/track?track=yes&trackNums=1ZY49W150314267379&requester=ST/trackdetails
#https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=4207618057019200190314714000726912
# your actual phone: https://www.ups.com/track?loc=en_US&tracknum=1ZE10Y190415481592&requester=SBCH&returnto=upsmychoice%3Floc%3Den_US%26tracknum%3D1ZE10Y190415481592/trackdetails
#
#
#
# RUN THE FOLLOWING COMMANDS IN COMMAND PROMPT BEFORE STARTING: 
# py -m pip install webdriver-manager
# py -m pip install -U selenium
# py -m pip install BeautifulSoup4
# py -m pip install twilio
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from webdriver_manager.firefox import GeckoDriverManager
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


account_sid = environ.get('TWILIO_ACCOUNT_SID')
auth_token = environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

refreshrate = 2

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(0.5)
driver.get('https://www.ups.com/track?loc=en_US&requester=ST/')

while True:
    try:
        l = driver.find_element(By.ID, 'st_App_DelvdLabel')
        print('Text obtained with text(): ' + l.text)
        break

    except NoSuchElementException:
        False
        driver.refresh()
        driver.implicitly_wait(0.5)

message = client.messages \
                .create(
                     body="Package has been Delivered",
                     from_='7817453686',
                     to='6822889402'
                 )

print(message.sid)
print("Text sent")

driver.quit()




#Another test package
# https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=9400109206094540159923
