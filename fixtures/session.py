from selenium.webdriver.common.by import By

class SessionHelper():

    def __init__(self, app, base_url):
        self.app = app
        self.base_url = base_url

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.CSS_SELECTOR, 'input[name="user"]').clear()
        wd.find_element(By.CSS_SELECTOR, 'input[name="user"]').send_keys(username)
        wd.find_element(By.CSS_SELECTOR, 'input[name="pass"]').click()
        wd.find_element(By.CSS_SELECTOR, 'input[name="pass"]').clear()
        wd.find_element(By.CSS_SELECTOR, 'input[name="pass"]').send_keys(password)
        wd.find_element(By.CSS_SELECTOR, 'input[value="Login"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()
        wd.get(self.base_url)

# проверка аунтификации:
    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

# проверка, что аунтификация выполнена под нужным пользователем:
    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

# получение имени пользователя
    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, "form.header b").text[1:-1]

# проверка при выходе из системы:
    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

# проверка при аунтификации:
    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)