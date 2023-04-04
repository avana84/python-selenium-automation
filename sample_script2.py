from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# init driver
driver = webdriver.Chrome(executable_path="/Users/anavisekruna/Desktop/Automation_QA/python-selenium-automation/chromedriver")
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)

#driver.implicitly_wait(5)  # check every 100 ms

# open the url
driver.get('https://www.google.com/')
# The below code is added to click on "Accept All" button on the "Before you continue to Google" dialog box
driver.find_element(By.ID, "L2AGLb").click()

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()  # checks for condition to be met every 500 ms

# click search
# driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()