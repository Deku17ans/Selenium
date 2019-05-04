from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\\onomo\\Documents\\Python\\Selenium\\chromedriver.exe')
driver.get('https://scs.cl.sophia.ac.jp/campusweb/campusportal.do')

#driver.set_window_size()

user_name = driver.find_element_by_name('userName')
#time.sleep(3)
user_name.send_keys('')
password = driver.find_element_by_name('password')
#time.sleep(3)
password.send_keys('')
password.submit()
