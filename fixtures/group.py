# класс помощник
class GroupHelper():

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

    def filling_fields(self, group):
        wd = self.app.wd
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.get("https://localhost/addressbook/group.php")

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.filling_fields(group)
        wd.find_element_by_name("submit").click()
        self.return_at_home_page()

    def modification(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector('input[name="edit"]').click()
        self.filling_fields(group)
        wd.find_element_by_name("update").click()
        self.return_at_home_page()

    def delete(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector('input[name="delete"]').click()
        self.return_at_home_page()

    def return_at_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))