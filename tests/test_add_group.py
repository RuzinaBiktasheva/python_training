# -*- coding: utf-8 -*-
from models.group import Group

# загрузка тестовых данных из json-файла (проверка списков объектов, загруженных из базы данных)
def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    # проверка по id и наименованию
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Проверка групп с БД
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# загрузка тестовых данных из json-файла
#def test_add_group(app, json_groups):
    #group = json_groups
    #old_groups = app.group.get_group_list()
    #app.group.create(group)
    #new_groups = app.group.get_group_list()
    # проверка по длине списка
    #assert len(old_groups) + 1 == len(new_groups)
    #old_groups.append(group)
    # проверка по id и наименованию
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)