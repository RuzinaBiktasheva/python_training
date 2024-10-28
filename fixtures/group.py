from models.group import Group

# класс помощник
class GroupHelper():

    def __init__(self, app, base_url):
        self.app = app
        self.base_url = base_url

    # проверка передачи параметров при вызове функции (поля для ввода)
    def type(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)
        else:
            pass

    # заполнение полей
    def filling_fields(self, group):
        wd = self.app.wd
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    # открытие страницы групп
    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()
        wd.get(self.base_url + 'group.php')

    # создание новой группы
    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.filling_fields(group)
        wd.find_element_by_name("submit").click()
        self.return_at_home_page()
        self.list_of_groups_cache = None

    # изменение первой группы
    def modification_first_group(self, group):
        self.modification_randon_group(group, 0)

    # изменение случайной группы
    def modification_randon_group(self, group, index):
        wd = self.app.wd
        self.open_group_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector('input[name="edit"]').click()
        self.filling_fields(group)
        wd.find_element_by_name("update").click()
        self.return_at_home_page()
        self.list_of_groups_cache = None

    # удаление первой группы
    def delete_first_group(self):
        self.delete_random_group(0)

    # удаление случайной группы
    def delete_random_group(self, index):
        wd = self.app.wd
        self.open_group_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector('input[name="delete"]').click()
        self.return_at_home_page()
        self.list_of_groups_cache = None

    # возврат на домашнюю страницу
    def return_at_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    # подсчет количества групп
    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    list_of_groups_cache = None

    # получение списка групп
    def get_group_list(self):
        if self.list_of_groups_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.list_of_groups_cashe = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.list_of_groups_cashe.append(Group(name=text, id=id))
        return list(self.list_of_groups_cashe)