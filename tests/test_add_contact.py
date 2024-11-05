# -*- coding: utf-8 -*-
from models.contact import Contact

# загрузка тестовых данных из json-файла (проверка списков объектов, загруженных из базы данных)
def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    # проверка по длине списка
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    # проверка по id, имени и фамилии
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# загрузка тестовых данных из json-файла
#def test_add_contact(app, json_contacts):
    #contact = json_contacts
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create(contact)
    #new_contacts = app.contact.get_contact_list()
    # проверка по длине списка
    #assert len(old_contacts) + 1 == len(new_contacts)
    #old_contacts.append(contact)
    # проверка по id, имени и фамилии
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)