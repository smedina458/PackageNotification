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
from flask import Flask, request, render_template


# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/index.py', methods =["GET", "POST"])
def get_input():
    if request.method == "POST":
       # getting input with freq = set_freq in HTML form
       phonenumber = request.form.get("phonenumber") # <--- get your variables
       trackingnumber = request.form.get("trackingnumber")
       carrier = request.form.get("carrier")
       return "Your values are " + trackingnumber, phonenumber, carrier
    return render_template("index.html")
  
if __name__=='__main__':
   app.run()






#form = cgi.FieldStorage
#
#
#app = Flask(__name__)
#
#@app.route('/index', methods=['GET','POST'])
#def my_form_post():
#    trackingnumber = request.form['trackingnumber']
#    phonenumber = request.form['phonenumber']
#    carrier = request.form['carrier']
#    return trackingnumber, phonenumber, carrier, render_template("index.html")
#
#
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver.implicitly_wait(0.5)
#driver.get('https://www.ups.com/track?loc=en_US&requester=ST/')
#
#trackingnumber = form.getvalue("trackingnumber")
#carrier = form.getvalue("carrier")
#
#inputElement = driver.find_element_by_id("stApp_trackingNumber")
#inputElement.send_keys('1')