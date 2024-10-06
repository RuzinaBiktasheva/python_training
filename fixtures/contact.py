from selenium.webdriver.support.ui import Select
from models.contact import Contact

# класс помощник
class ContactHelper():

    def __init__(self, app):
        self.app = app

    def filling_fields(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def create(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.get("https://localhost/addressbook/edit.php")
        self.filling_fields(Contact(firstname="First_name", middlename="Middle_name", lastname="Last_name", nickname="Nickname", title="Title", company="Company", address="Address",
                               home="Telephone_home", mobile="Telephone_mobile", work="Telephone_work", fax="Telephone_fax", email="email",
                               email2="email_2", email3="email_3", homepage="homepage", bday='1', bmonth='January', byear='2000', aday='2', amonth='February', ayear='2010'))
        wd.find_element_by_name("submit").click()
        self.return_at_home_page()

    def modification(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.get("https://localhost/addressbook/#")
        wd.find_element_by_css_selector('img[src="icons/status_online.png"]').click()
        wd.find_element_by_css_selector('input[name="modifiy"]').click()
        self.filling_fields(Contact(firstname="New_first_name", middlename="New_middle_name", lastname="New_last_name", nickname="New_nickname", title="New_title", company="New_company", address="New_address",
                               home="New_telephone_home", mobile="New_telephone_mobile", work="New_telephone_work", fax="New_telephone_fax", email="New_email",
                               email2="New_email_2", email3="New_email_3", homepage="New_homepage", bday='2', bmonth='February', byear='2001', aday='3', amonth='March', ayear='2011'))
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