from selenium.webdriver.support.ui import Select
from models.contact import Contact
import os
import re

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

    def added_file(self):
        wd = self.app.wd
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test.txt')
        wd.find_element_by_css_selector('input[name="photo"]').send_keys(file_path)

    # открытие страницы контактов
    def open_contact_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_css_selector('input[value="Send e-Mail"]')) > 0):
            wd.find_element_by_link_text("home").click()
            wd.get("https://localhost/addressbook/#")

    # заполнение полей
    def filling_fields(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("middlename", contact.middlename)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.added_file()
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

    # создание контакта
    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.get("https://localhost/addressbook/edit.php")
        self.filling_fields(contact)
        wd.find_element_by_name("submit").click()
        self.return_at_home_page()
        self.list_of_contacts_cache = None

    # изменение первого контакта
    def modification_first_contact(self):
        self.modification_random_contact(0)

    # изменение случайного контакта
    def modification_random_contact(self, contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.filling_fields(contact)
        wd.find_element_by_name("update").click()
        self.return_at_home_page()
        self.list_of_contacts_cache = None

    # удаление первого контакта
    def delete_first_contact(self):
        self.delete_random_contact(0)

    # удаление случайного контакта
    def delete_random_contact(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        wd.find_element_by_css_selector('input[value="Delete"]').click()
        self.return_at_home_page()
        self.list_of_contacts_cache = None

    # возврат на домашнюю страницу
    def return_at_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    # подсчет количества контактов
    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_css_selector('img[src="icons/status_online.png"]'))

    list_of_contacts_cache = None

    # получение информации о контакте с главной страницы
    def get_contact_list(self):
        if self.list_of_contacts_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.list_of_contacts_cache = []
            for element in wd.find_elements_by_css_selector('tr[name="entry"]'):
                firstname = element.find_element_by_xpath('td[3]').text
                lastname = element.find_element_by_xpath('td[2]').text
                id =  element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_xpath('td[6]').text.splitlines()
                self.list_of_contacts_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, home=all_phones[0], mobile=all_phones[1], work=all_phones[2]))
        return list(self.list_of_contacts_cache)

    # открытие контакта на редактирование / удаление (по индексу)
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_css_selector('img[src="icons/pencil.png"]')[index].click()

    # открытие контакта на просмотр (по индексу)
    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_css_selector('img[src="icons/status_online.png"]')[index].click()

    # получение информации с карточки редактирования контакта
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=homephone, mobile=mobilephone, work=workphone)

    # получение информации с карточки просмотра контакта
    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        return Contact(home=homephone, mobile=mobilephone, work=workphone)