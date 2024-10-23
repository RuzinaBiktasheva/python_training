# -*- coding: utf-8 -*-
from models.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name='', header='', footer='')] + [
    Group(name=random_string('name:', 10), header=random_string('header:', 20), footer=random_string('footer:', 30))
    for i in range(5)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    # проверка по длине списка
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    # проверка по id и наименованию
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)