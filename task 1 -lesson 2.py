#Amazon Logo
driver.find_element(By.XPATH, “//i[@aria-label='Amazon']")

# Email field
driver.find_element(By.XPATH, “//label[@for='ap_email']")

#Continue button
driver.find_element(By.XPATH, “//input[@id='continue']")

# Need help link
driver.find_element(By.XPATH, “//span[@class='a-expander-prompt']")

# Forgot your password link - multiple attributes
driver.find_element(By.XPATH, “//a[@class='a-link-normal' and @id='auth-fpp-link-bottom']")

# By XPath, Other issues - multiple attributes
driver.find_element(By.XPATH, “//a[@class='a-link-normal' and @id='ap-other-signin-issues-link']")

# Create your Amazon account button
driver.find_element(By.XPATH, “//a[@class='a-button-text']")

# *Conditions of use link - by text
driver.find_element(By.XPATH, “//a[text()='Conditions of Use']")

# *Privacy Notice link by text
driver.find_element(By.XPATH, “ // a[text() = 'Privacy Notice']")


