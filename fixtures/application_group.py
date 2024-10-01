from selenium.webdriver.firefox.webdriver import WebDriver
from fixtures.group import GroupHelper
from fixtures.session import SessionHelper

# фикстура для теста добавления группы:
class ApplicationGroup:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/#")

    def destroy(self):
        self.wd.quit()