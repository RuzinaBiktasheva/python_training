# класс помощник
class GroupHelper():

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.get("https://localhost/addressbook/group.php")
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_at_home_page()

    def modification(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.get("https://localhost/addressbook/group.php")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector('input[name="edit"]').click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
        self.return_at_home_page()

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.get("https://localhost/addressbook/group.php")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector('input[name="delete"]').click()
        self.return_at_home_page()

    def return_at_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()