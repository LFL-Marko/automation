from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.guest_list_page import GuestListElements

from data.config import settings
from urllib.parse import urljoin

chrome_options = Options()

class WebApp():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        if str(settings['browser']).lower() == 'chrome':
            self.driver = webdriver.Chrome(
                executable_path='/usr/local/bin/drivers/chromedriver', options=chrome_options)
        elif str(settings['browser']).lower == 'firefox':
            self.driver = webdriver.Geckodriver()
    
    def get_driver(self):
        return self.driver

    def load_website(self, url):
        self.driver.get(settings['url'])

    # add to the settings.json so that the page url can be accessed as well
    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def verify_component_exists(self, component):
        assert component in self.driver.find_element_by_class_name().text, \
            "Component {} not found on page".format(component)

webapp = WebApp.get_instance()