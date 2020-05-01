from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS_HEADER = (By.XPATH, '//h3//span')
RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)


@when('Tap Enter to search')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys(Keys.ENTER)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    search_result_header = context.driver.find_element(*RESULTS_HEADER).text
    assert 'Dress' in search_result_header, f'Incorrect header: {search_result_header}'


@then('First result contains {search_word}')
def verify_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    assert search_word in first_result, f"Expected word '{search_word}' in message, but got '{first_result}'"
