from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

songURL = raw_input("Enter Song Youtube URL:")

driver = webdriver.Chrome("C:\Python27\Lib\site-packages\selenium\chromedriver\chromedriver.exe")
driver.get("https://ytmp3.cc/")
print(driver)
driver.find_element_by_id("input").send_keys(songURL)
driver.find_element_by_id("submit").click()
driver.implicitly_wait(20)
driver.find_element_by_id("download").click()
time.sleep(10)
driver.quit()