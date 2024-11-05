# -*- coding: utf-8 -*-
from models.contact import Contact
import random


# удаление контакта с помощью БД по id (проверка списков объектов, загруженных из базы данных)
def test_delete_contact_by_id(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First_name_for_delete"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    # проверка по длине списка
    assert len(old_contacts) - 1 == len(new_contacts)
    # Удаление контакта
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    # Проверка контактов с БД
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# удаление случайного контакта
#def test_delete_random_contact(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="First_name_for_delete"))
    #old_contacts = app.contact.get_contact_list()
    # индекс случайного контакта:
    #index = randrange(len(old_contacts))
    #app.contact.delete_random_contact(index)
    #new_contacts = app.contact.get_contact_list()
    # проверка по длине списка
    #assert len(old_contacts) - 1 == len(new_contacts)
    # Удаление контакта
    #del old_contacts[index:index+1]
    #assert old_contacts == new_contacts