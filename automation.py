import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import numpy as np
import warnings
import os
import gspread
import sys
from datetime import datetime
from selenium.webdriver.common.keys import Keys
# For connect to google sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials

PATH = os.getcwd()
CHROME_DRIVER_PATH = PATH+'/chromedriver'
driver = webdriver.Chrome(CHROME_DRIVER_PATH,options=options)


driver.get('.com')
time.sleep(10)
em = driver.find_element_by_xpath("//input[@placeholder = 'Email']").send_keys("@gmail.com")
time.sleep(20)
pw = driver.find_element_by_xpath("//input[@placeholder = 'Password']").send_keys("*****")
time.sleep(20)
clic = driver.find_element_by_xpath("//input[@value= 'Log in']")
clic.click()
time.sleep(10)
driver.find_element_by_xpath("//button[text()='skip']")
time.sleep(10)

def executeSomething(): 
    
    scope = ['https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('json',scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d//edit#gid=0")
    
    sheet5 = sheet.worksheet("Sheet5")
    sheet6 = sheet.worksheet("Sheet6")
    
    #converting to a dataframe
    rl_delete =  gd.get_as_dataframe(sheet5,evaluate_formulas = True,skiprows = 0,has_header = True)
    ulp_delete =  gd.get_as_dataframe(sheet6,evaluate_formulas = True,skiprows = 0,has_header = True)
   
    #drop null values
    rl_delete1 = ndp_dup_rotational_delete[['id']].dropna()
    ulp_delete1 = ndp_dup_ulp_delete[['id']].dropna() 
    
    
    driver.get("https://.com/")
    time.sleep(5)
    driver.refresh()
    time.sleep(3)
    vehicle_button = driver.find_element_by_xpath("//button[text()='veh']")
    vehicle_button.click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[text()='Manual']")
    time.sleep(3)
    driver.find_element_by_xpath("//div[text()='Maximum 5000 IDs'] /..//textarea").send_keys(rl_delete1)
    time.sleep(3)
    b1 = Select(driver.find_element_by_xpath("//span[text()='TRANSFORMATION']/../..//select"))
    b1.select_by_visible_text("DELETE")
    time.sleep(3)
    
while True:
      time.sleep(600)
        try:
           aa = driver.find_element_by_xpath("//button[.='ACKNOWLEDGE AND ACCEPT']")
           aa.click()
       except:
           try:
               executeSomething()
           except:
                 pass 
