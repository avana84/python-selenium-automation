from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy')
PRIVACY_TITLE = (By.CSS_SELECTOR, "article.help-content h1")

@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original window')
def store_current_window(context):
    context.current_window = context.driver.current_window_handle
    print(context.current_window)

@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()

@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])

@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    actual_text = context.driver.find_element(*PRIVACY_TITLE).text
    expected_text = "Amazon.com Privacy Notice"
    assert expected_text == actual_text, f'expected{expected_text} but got {actual_text}'


@then('User can close new window and switch back to original')
def verify_user_can_close_new_window_and_switch_back_to_original(context):
    context.driver.switch_to.window(context.current_window)













