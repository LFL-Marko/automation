from framework.webapp import webapp
from pages.guest_list_page import GuestListPage
from allure_behave.hooks import allure_report


def before_all(context):
    # to access more logic for steps and store them in context
    # as well as store page variables 
    context.gl_el = GuestListElements
    

def after_step(context, step):
    print("")
    
def after_all(context):
    webapp.driver.quit()

# allure_report("path/to/result/dir")