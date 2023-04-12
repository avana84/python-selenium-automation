from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.current_window = context.driver.current_window_handle
    print.(context.current_window)


@when('Store original windows')
def store_original_window(context):
    context.driver.find.element().click()


