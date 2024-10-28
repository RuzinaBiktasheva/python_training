import pytest
import json
import os.path
from fixtures.application import Application

fixture = None
target = None

# инициализация фикстуры
@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    path = request.config.getoption('--path')
    if target is None:
        config_file = os.path.join(path, request.config.getoption('--target'))
        with open(config_file) as file:
            target = json.load(file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'], path=path)
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


# финализация фикстуры:
@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

# инициализация параметров
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')
    parser.addoption('--path', action='store', default='C:/training/python_training')