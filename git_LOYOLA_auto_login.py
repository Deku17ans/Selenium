from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\\onomo\\Documents\\Python\\Selenium\\chromedriver.exe')
driver.get('https://scs.cl.sophia.ac.jp/campusweb/campusportal.do')

user_name = driver.find_element_by_name('userName')
user_name.send_keys('ユーザー名')

password = driver.find_element_by_name('password')
password.send_keys('パスワード')
password.submit()
