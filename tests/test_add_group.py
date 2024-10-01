# -*- coding: utf-8 -*-
import pytest
from models.group import Group
from fixtures.application import Application

# инициализация фикстуры
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create(Group(name="name", header="header", footer="footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create(Group(name="", header="", footer=""))
    app.logout()