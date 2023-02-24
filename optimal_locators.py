from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/anavisekruna/Desktop/Automation_QA/python-selenium-automation/chromedriver')

#By CSS, using ID (tag#id)
driver.find_element(By.CSS_SELECTOR

#Create account - By CSS class
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#Your name - tag[attribute=value
driver.find_element(By.CSS_SELECTOR, "label[for=ap_customer_name]")

#Email - tag[attribute=value]
driver.find_element(By.CSS_SELECTOR, "label[for=ap_email]")

#Password - tag[attribute=value]
driver.find_element(By.CSS_SELECTOR, "label[for=ap_password]")

#Re-enter password - tag[attribute=value]
driver.find_element(By.CSS_SELECTOR, "label[for=ap_password_check]")