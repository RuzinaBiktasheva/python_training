# -*- coding: utf-8 -*-
from models.group import Group

def test_modification_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_delete", header="Header_for_delete", footer="Footer_for_delete"))
    app.group.modification(Group(name="New_name", header="New_header", footer="New_footer"))