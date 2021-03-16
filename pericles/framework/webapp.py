from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as ff_Options
from data.config import settings
# from printerror import PrintException

chrome_options = Options()
firefox_options = ff_Options()
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
                executable_path='/usr/local/bin/drivers/chromedriver',
                options=chrome_options)
        elif str(settings['browser']).lower() == 'firefox':
            self.driver = webdriver.Firefox(
                executable_path='/usr/local/bin/drivers/geckodriver',
                options=firefox_options)
    
    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    # add to the settings.json so that the page url can be accessed as well
    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def verify_component_exists(self, component):
        assert component in self.driver.find_element_by_class_name().text, \
            "Component {} not found on page".format(component)

webapp = WebApp.get_instance()