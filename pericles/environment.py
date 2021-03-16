from framework.webapp import webapp
from pages.guest_list_page import GuestListElements
from allure_behave.hooks import allure_report


def before_all(context):
    context.guest_list_url = GuestListElements.GUEST_LIST_URL
    
def after_step(context, step):
    print("")
    
def after_all(context):
    webapp.driver.quit()

# allure_report("path/to/result/dir")