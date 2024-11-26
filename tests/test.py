from selenium import webdriver


driver = webdriver.Firefox()


# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://localhost/addressbook/#")