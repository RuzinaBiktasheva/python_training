from selenium import webdriver
from fixtures.group import GroupHelper
from fixtures.session import SessionHelper
from fixtures.contact import ContactHelper

# класс менеджер:
class Application():

    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            raise ValueError('Unrecognized browser:')# ' f'{browser}')
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

# проверка валидности фикстуры:
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()