# -*- coding: utf-8 -*-
from models.contact import Contact
from random import randrange

def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First_name_for_delete"))
    old_contacts = app.contact.get_contact_list()
    # индекс случайного контакта:
    index = randrange(len(old_contacts))
    app.contact.delete_random_contact(index)
    new_contacts = app.contact.get_contact_list()
    # проверка по длине списка
    assert len(old_contacts) - 1 == len(new_contacts)
    # Удаление контакта
    del old_contacts[index:index+1]
    assert old_contacts == new_contacts