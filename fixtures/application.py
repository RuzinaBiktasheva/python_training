from selenium.webdriver.firefox.webdriver import WebDriver
from fixtures.group import GroupHelper
from fixtures.session import SessionHelper
from fixtures.contact import ContactHelper

# класс менеджер:
class Application():

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

# проверка валидности фикстуры:
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/#")

    def destroy(self):
        self.wd.quit()