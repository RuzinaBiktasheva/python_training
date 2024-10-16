# -*- coding: utf-8 -*-
from models.group import Group

def test_modification_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_delete", header="Header_for_delete", footer="Footer_for_delete"))
    old_groups = app.group.get_group_list()
    added_group = Group(name="New_name", header="New_header", footer="New_footer")
    added_group.id = old_groups[0].id
    app.group.modification(added_group)
    new_groups = app.group.get_group_list()
    # проверка по длине списка
    assert len(old_groups) == len(new_groups)
    old_groups[0] = added_group
    # проверка по id и наименованию группы
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)