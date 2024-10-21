# класс помощник
class SessionHelper():

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.get("https://localhost/addressbook/#")

# проверка аунтификации:
    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

# проверка, что аунтификация выполнена под нужным пользователем:
    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

# получение имени пользователя
    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

# проверка при выходе из системы:
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

# проверка при аунтификации:
    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)