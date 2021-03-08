from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from behave import *
import environment
import time
from framework.webapp import webapp
from pages import guest_list_page
from printerror import PrintException

driver = webapp.get_driver()
wt = WebDriverWait(driver, 5)

@given('I go to the admin page')
def i_log_in_as(context):
    try:
        webapp.load_website()
    except Exception as error:
        print(error)
        
@when(u'I navigate to the "{url}"')
def i_navigate_to_page(context, url):
    print("I am navigating!")

@when('I click on the "{cta}t" cta')
def i_click_on_the_cta(context, cta):
    try:
        gl_el = wt.until(
            EC.presence_of_element_located((By.LINK_TEXT,
            "Guest List")))
        gl_el.click()
    except Exception as error:
        PrintException(error)

@then('I will be navigated to the "{page}" page')
def i_will_be_navigated_to_the_page(context, page):
    try:
        url = driver.current_url
        assert url == "https://admin-meraki-qa.eventably.co/guests/list"
    except Exception as error:
        PrintException(error)
