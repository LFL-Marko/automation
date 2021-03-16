from selenium.webdriver.common.by import By
from framework.webapp import webapp
from printerror import PrintException


class GuestListElements(object):
    """
    Page elements for the Guest List page
    """

    GUEST_LIST_URL = (By.XPATH,
    'https://admin-meraki-qa.eventably.co/guests/list')
    GUEST_LIST_CTA = (By.XPATH,
    '//*[@id="root"]/div/div[1]/ul/li[11]/a')
    PAGE_HEADING = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/h2')
    TOTAL_REGS = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[1]/div[2]/span[2]')
    ADD_ATTENDEE = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[2]/table/tbody/tr[1]/td[5]/div/button')
    UPLOAD_CSV = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[1]/div[1]/div[2]/button')
    DOWNLOAD_CSV = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[1]/div[1]/button')
    USER_NAME = (By.XPATH,
    '//*[@id="root"]/div/div[2]/header/ul[2]/p')
    USER_AVATAR = (By.XPATH,
    '//*[@id="root"]/div/div[2]/header/ul[2]/li/a/div/img')
    FILTER_INPUT = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[1]/input')
    ITEMS_PER_PAGE_DROPDOWN = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select')
    CURRENT_ITEMS_PP = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[1]')
    ITEMS_50_PP = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[2]')
    ITEMS_20_PP = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[3]')
    ITEMS_10_PP = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[4]')
    ITEMS_5_PP = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[5]')
    PAGINATION_BEGIN = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/nav/ul/li[1]')
    PAGINATION_END = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/nav/ul/li[7]')
    PAGINATION_PREVIOUS = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/nav/ul/li[2]')
    PAGINATION_NEXT = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/nav/ul/li[6]')
    COLUMN_HEADERS = (By.XPATH,
    '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[2]/table/thead/tr')
    # include '[<indece starting with 1>]' for each guest row
    ## number of rows should match CURRENT_ITEMS_PP
    DATE_ADDED_COL = '/th[1]'
    FIRST_NAME_COL = '/th[2]'
    LAST_NAME_COL = '/th[3]'
    EMAIL_ADDRESS_COL = '/th[4]'
    ROLE_COL = '/th[5]'
    STATUS_COL = '/th[6]'
    SORT_ARROW = '/svg'


class GuestListPage():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = GuestListPage()
        return cls.instance


    def __init__(self):
        self.driver = webapp.get_driver()


    # def get_url(self):
        # webapp.get_url() = self.driver.current_url


    # def verify_url(self,expected_url):
    #     expected_url = GuestListPage.format(expected_url)
    #     print(url)
    #     try:
    #         assert webapp.get_url() == expected_url
    #         "The URL is not the expected url for the Guest List page"\
    #                                         " Expected: {}, Actual: {}".format(expected_url, url)
    #         print("The page url is as expected.")
    #     except Exception as error:
    #         PrintException(error)
        

GUEST_LIST = GuestListPage.get_instance()