from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\onomo\\Documents\\Python\\Selenium\\chromedriver.exe')
driver.get('https://moodle.cc.sophia.ac.jp/login/index.php')

user = driver.find_element_by_name('username')
user.send_keys('ユーザー名')
login = driver.find_element_by_name('password')
login.send_keys('パスワード')
btn = driver.find_element_by_id('loginbtn')
btn.click()
