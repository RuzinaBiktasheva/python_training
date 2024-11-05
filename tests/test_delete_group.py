# -*- coding: utf-8 -*-
from models.group import Group
import random


# удаление группы с помощью БД по id (проверка списков объектов, загруженных из базы данных)
def test_delete_group_by_id(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Name_for_delete", header="Header_for_delete", footer="Footer_for_delete"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    # проверка по длине списка
    assert len(old_groups) - 1 == len(new_groups)
    # Удаление группы
    old_groups.remove(group)
    assert old_groups == new_groups
    # Проверка групп с БД
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# удаление случайной группы
#def test_delete_random_group(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="Name_for_delete", header="Header_for_delete", footer="Footer_for_delete"))
    #old_groups = app.group.get_group_list()
    # индекс случайной группы:
    #index = randrange(len(old_groups))
    #app.group.delete_random_group(index)
    #new_groups = app.group.get_group_list()
    # проверка по длине списка
    #assert len(old_groups) - 1 == len(new_groups)
    # Удаление группы
    #old_groups[index:index+1] = []
    #assert old_groups == new_groups