from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@when ('Click on add to cart button')
def click_on_add_to_cart_button (context):
    context.driver.find_element(By.XPATH, "//input[@name='submit.addToCart']").click()


@when('Open cart page')
def open_cart_page (context):
    context.driver.find.element(By.ID, "//span[@id='nav-cart-count']").click()


# @then ('Verify that cart has 1 item')
# def verify_cart_count(context, expected_count):
# #i do not know how to do this


