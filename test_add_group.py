# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(executable_path=r'C:/Windows/SysWOW64/geckodriver.exe')
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("https://localhost/addressbook/#")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()
        wd.get("https://localhost/addressbook/group.php")

    def create_new_group(self, wd, name, header, footer):
        wd.find_element_by_name("new").click()
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        wd.find_element_by_name("submit").click()

    def return_at_list_groups(self, wd):
        wd.find_element_by_link_text("groups").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
    
    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_group_page(wd)
        self.create_new_group(wd, "name", "header", "footer")
        self.return_at_list_groups(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_group_page(wd)
        self.create_new_group(wd, "", "", "")
        self.return_at_list_groups(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
