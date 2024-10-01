from selenium.webdriver.firefox.webdriver import WebDriver
from fixtures.session import SessionHelper
from fixtures.contact import ContactHelper

# фикстура для теста добавления контакта:
class ApplicationContact:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/#")

    def destroy(self):
        self.wd.quit()