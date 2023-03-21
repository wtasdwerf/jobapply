import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('info.json', 'r') as f:
    credentials = json.load(f)

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3478691444&f_AL=true&geoId=105149562&keywords=python%20developer&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&refresh=true")

login_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")

login_button.click()

id = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
pw = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
login_button2 = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

id.send_keys(credentials['username'])
pw.send_keys(credentials['password'])
login_button2.click()

time.sleep(10)

driver.quit()