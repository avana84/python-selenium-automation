from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
@when('Click on cart icon')
def click_on_cart_icon(context):
    sleep(1)
    context.driver.find_element(By.ID, "nav-cart").click()

@then('Verify that you see your cart is empty message')
def verify_cart_is_empty_message(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    assert expected_result == actual_result, f"Expected text {expected_result}, but got {actual_result}"

