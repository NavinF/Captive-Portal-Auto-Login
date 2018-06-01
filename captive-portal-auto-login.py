#!/usr/bin/env python3

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.chrome.options

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)
chrome_options = selenium.webdriver.chrome.options.Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://neverssl.com/')
wait_seconds = 8
driver.implicitly_wait(wait_seconds)
wait = WebDriverWait(driver, wait_seconds)
selectors = ['#SubmitButton']
for selector in selectors:
    try:
        driver.find_element_by_css_selector(selector).click()
        print("Clicked submit button.")
        wait.until(expected_conditions.title_contains("Successful"))
        print("Logged In.")
        break
    except WebDriverException as e:
        logger.info(f"Ignoring WebDriverException: {e}")
else:
    print("Failed (?) to login")
driver.quit()
