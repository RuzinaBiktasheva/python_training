from selenium.webdriver.support.ui import Select
from models.contact import Contact

# класс помощник
class ContactHelper():

    def __init__(self, app):
        self.app = app

    # проверка передачи параметров при вызове функции (поля для ввода)
    def type(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)
        else:
            pass

    # проверка передачи параметров при вызове функции (выпадающий список)
    def type_list(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(field_value)
        else:
            pass

    def filling_fields(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("middlename", contact.middlename)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("title", contact.title)
        self.type("company", contact.company)
        self.type("address", contact.address)
        self.type("home", contact.home)
        self.type("mobile", contact.mobile)
        self.type("work", contact.work)
        self.type("fax", contact.fax)
        self.type("email", contact.email)
        self.type("email2", contact.email2)
        self.type("email3", contact.email3)
        self.type("homepage", contact.homepage)
        self.type_list("bday", contact.bday)
        self.type_list("bmonth", contact.bmonth)
        self.type("byear", contact.byear)
        self.type_list("aday", contact.aday)
        self.type_list("amonth", contact.amonth)
        self.type("ayear", contact.ayear)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.get("https://localhost/addressbook/edit.php")
        self.filling_fields(contact)
        wd.find_element_by_name("submit").click()
        self.return_at_home_page()

    def modification(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.get("https://localhost/addressbook/#")
        wd.find_element_by_css_selector('img[src="icons/status_online.png"]').click()
        wd.find_element_by_css_selector('input[name="modifiy"]').click()
        self.filling_fields(contact)
        wd.find_element_by_name("update").click()
        self.return_at_home_page()

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.get("https://localhost/addressbook/#")
        wd.find_element_by_css_selector('img[src="icons/status_online.png"]').click()
        wd.find_element_by_css_selector('input[name="modifiy"]').click()
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        self.return_at_home_page()

    def return_at_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()