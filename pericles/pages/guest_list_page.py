from framework.webapp import webapp


class GuestListElements(object):

    ADD_ATTENDEE = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[2]/div[2]/table/tbody/tr[1]/td[5]/div/button'
    UPLOAD_CSV = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[1]/div[1]/div[2]/button'
    DOWNLOAD_CSV = '//*[@id="root"]/div/div[2]/div/main/div/div/div/section[1]/div[1]/button'
    USER_NAME = '//*[@id="root"]/div/div[2]/header/ul[2]/p'
    USER_AVATAR = '//*[@id="root"]/div/div[2]/header/ul[2]/li/a/div/img'
    


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
