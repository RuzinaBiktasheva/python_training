# -*- coding: utf-8 -*-
from models.group import Group
from random import randrange

def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_delete", header="Header_for_delete", footer="Footer_for_delete"))
    old_groups = app.group.get_group_list()
    # индекс случайной группы:
    index = randrange(len(old_groups))
    app.group.delete_random_group(index)
    new_groups = app.group.get_group_list()
    # проверка по длине списка
    assert len(old_groups) - 1 == len(new_groups)
    # Удаление группы
    old_groups[index:index+1] = []
    assert old_groups == new_groups