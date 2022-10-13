# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:44:47 2022

@author: zsk
"""
from selenium import webdriver
from time import sleep


#kolegij = input('Odaberi kolegij (M1/M2):')
#print('Odabrani kolegij je:', kolegij)
"""
Dio koda koji dkida zadnje prijavljene studente
"""

username = "dturk@unisb.hr"
password = "gtr456tgh"

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"D:\asistent_sfsb\mehanika2"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--window-size=1920,1080')
chromedriver = r"C:\python_drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

driver.get("https://www.isvu.hr/nastavnickiportal/hr/prijava")

driver.find_element_by_class_name("linkSamlPrijava").click()
sleep(.5)
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("login-btn").click()
sleep(.5)
driver.get("https://www.isvu.hr/nastavnickiportal/hr/ispit/ispitnirok")
sleep(.5)

driver.find_element_by_xpath("//form[@id='form_218728']//a[@title='Dohvati']").click()

sleep(.5)
#Meha2
driver.find_element_by_xpath("//span[normalize-space()='Excel']").click()

sleep(1)
driver.close()