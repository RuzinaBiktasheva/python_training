# -*- coding: utf-8 -*-
from models.group import Group

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_delete", header="Header_for_delete", footer="Footer_for_delete"))
    old_groups = app.group.get_group_list()
    app.group.delete()
    new_groups = app.group.get_group_list()
    # проверка по длине списка
    assert len(old_groups) - 1 == len(new_groups)
    # Удаление первой группы
    old_groups[0:1] = []
    assert old_groups == new_groups