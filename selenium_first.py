import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://urbantheka.in/")
time.sleep(3)
element = driver.find_element(By.CLASS_NAME, "w-full px-4 py-3 flex items-center justify-between")
