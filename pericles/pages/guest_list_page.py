from framework.webapp import webapp


class GuestListElements(object):

    PAGE_HEADING = '//*[@id="root"]/div/div[2]/div/main/div/div/div/h2'
    TOTAL_REGS = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[1]/div[2]/span[2]'
    ADD_ATTENDEE = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[2]/table/tbody/tr[1]/td[5]/div/button'
    UPLOAD_CSV = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[1]/div[1]/div[2]/button'
    DOWNLOAD_CSV = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[1]/div[1]/button'
    USER_NAME = '//*[@id="root"]/div/div[2]/header/ul[2]/p'
    USER_AVATAR = '//*[@id="root"]/div/div[2]/header/ul[2]/li/a/div/img'
    FILTER_INPUT = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[1]/input'
    ITEMS_PER_PAGE_DROPDOWN = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select'
    CURRENT_ITEMS_PP = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[1]'
    ITEMS_50_PP = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[2]'
    ITEMS_20_PP = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[3]'
    ITEMS_10_PP = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[4]'
    ITEMS_5_PP = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[1]/div/div[2]/div/select/option[5]'
    PAGINATION_BEGIN = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/nav/ul/li[1]'
    PAGINATION_END = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/nav/ul/li[7]'
    PAGINATION_PREVIOUS = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/nav/ul/li[2]'
    PAGINATION_NEXT = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/nav/ul/li[6]'
    COLUMN_HEADERS = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[2]/table/thead/tr'
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

    def verify_url(self, url):
        url = self.driver.current_url()
        assertEqual(url, "https://admin-meraki-qa.eventably.co/guests/list")

guest_list = GuestListPage.get_instance()
