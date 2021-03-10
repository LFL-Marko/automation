from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from behave import *
import environment
import time
from framework.webapp import webapp
from pages.guest_list_page import GuestListElements as EL
from printerror import PrintException

driver = webapp.get_driver()
wt = WebDriverWait(driver, 11)

@given('I go to the admin page')
def i_log_in_as(context):
    webapp.load_website()
    wt.until(
        EC.presence_of_element_located((By.LINK_TEXT,
        "Guest List")))

        
@when(u'I navigate to the "{url}"')
def i_navigate_to_page(context, url):
    print("I am navigating!")

@when('I click on the "{cta}" cta')
def i_click_on_the_cta(context, cta):
    driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/ul/li[11]/a').click()
    print("I need to click here")


@then('I will be navigated to the Guest List page')
def i_will_be_navigated_to_the_page(context):
    wt.until(
        EC.visibility_of_element_located((By.XPATH,
        "//*[@id='root']/div/div[2]/div/main/div/div/div/section[1]/div[1]/div[1]/button")))
    url = driver.current_url
    print(url)
    expected_url = "https://admin-meraki-qa.eventably.co/guests/list"
    assert url == expected_url, "The URL is not the expected url for the Guest List page"\
                                        " Expected: {}, Actual: {}".format(expected_url, url)
    print("The page url is as expected.")

