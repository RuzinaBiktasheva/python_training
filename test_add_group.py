# -*- coding: utf-8 -*-
import pytest
from group import Group
from application_group import ApplicationGroup

@pytest.fixture
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="name", header="header", footer="footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()