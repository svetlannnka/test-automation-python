from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='put_your_path_here')

# Open a page
driver.get('https://www.google.com/')
driver.implicitly_wait(4)

search_field = driver.find_element(By.NAME, 'q')
search_field.send_keys('Dress', Keys.ENTER)

# Verify header
search_result_header = driver.find_element(By.XPATH, '//h3//span').text
assert 'Dress' in search_result_header, f'Incorrect header: {search_result_header}'

driver.quit()