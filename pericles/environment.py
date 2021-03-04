from framework.webapp import webapp
from pages.guest_list_page import GuestListPage

def before_all(context):
    # to access more logic for steps and store them in context
    # as well as store page variables 
    context.guest_list = GuestListPage()

def after_step(context, step):
    print("")
    
def after_all(context):
    webapp.driver.quit()