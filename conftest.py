import pytest
import json
import os.path
import importlib
import jsonpickle
from fixtures.application import Application
from fixtures.db import DbFixture

fixture = None
target = None


# загрузка конфигурации из файла target.json
def load_config(file):
    global target
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    if target is None:
        config_file = os.path.join(path, file)
        with open(config_file) as file:
            target = json.load(file)
    return target

# инициализация фикстуры
@pytest.fixture
def app(request):
    global fixture
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    web_config = load_config(request.config.getoption('--target'))['web']
    browser = request.config.getoption('--browser')
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


# инициализация фикстуры БД
@pytest.fixture (scope="session")
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


# инициализация фикстуры маркера проверок на Ui
@pytest.fixture
def check_ui(request):
    return request.config.getoption('--check_ui')


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
    parser.addoption('--check_ui', action='store_true')

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith('json_'):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/%s.json') % file) as f:
        return jsonpickle.decode(f.read())