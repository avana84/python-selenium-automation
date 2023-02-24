from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on Returns & Orders')
def click_on_returns_orders(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

@then('Verify that Sign in page opened')
def verify_sign_in_result(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'

@when('Input book')
def input_book (context):
    context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Book")

@when('Click on search button')
def click_on_search_button (context):
    context.driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()


@when("Click on the first product")
def step_impl(context):
    sleep(2)
    all_books = context.driver.find_elements(By.XPATH, "//div[@id='gridItemRoot']/div[2]/div/span/div")
    all_books[0].click()
    sleep(2)
    pass


@then("Verify that cart has 1 item")
def step_impl(context):
    sleep(1)
    expected_text= "Subtotal (1 item):"
    actual_text = context.driver.find_element(By.ID, "sc-subtotal-label-activecart").text
    assert expected_text == actual_text, f"Expected text not found, but found {actual_text}"