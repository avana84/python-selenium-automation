from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon best sellers page')
def open_amazon_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify that header has {expected_count} links')
def verify_header_count(context, expected_count):
    all_links = context.driver.find_elements(By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']/ul/li/div/a")
    actual_count = len(all_links)
    assert expected_count == str(actual_count), f"Expected count to be {expected_count}, but got count as {actual_count}"
    #i dont know how to find the right element here(i need to finish HTML training for this maybe)
