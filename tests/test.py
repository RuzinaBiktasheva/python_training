from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:\Browsers\MozillaFirefox\firefox.exe"
service = Service(executable_path=r'C:\Windows\SysWOW64\geckodriver.exe')
wd = webdriver.Firefox(service=service, options=options)



# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
wd.get("https://localhost/addressbook/#")