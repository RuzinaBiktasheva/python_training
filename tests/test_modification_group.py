# -*- coding: utf-8 -*-
from models.group import Group

def test_modification_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification(Group(name="New_name", header="New_header", footer="New_footer"))
    app.session.logout()