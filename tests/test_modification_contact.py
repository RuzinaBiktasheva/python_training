# -*- coding: utf-8 -*-
from models.contact import Contact
from random import randrange

def test_modification_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First_name_for_delete"))
    old_contacts = app.contact.get_contact_list()
    # индекс случайного контакта:
    index = randrange(len(old_contacts))
    modify_contact = Contact(firstname="New_first_name", middlename="New_middle_name", lastname="New_last_name", nickname="New_nickname", title="New_title", company="New_company", address="New_address",
                               home="New_telephone_home", mobile="New_telephone_mobile", work="New_telephone_work", fax="New_telephone_fax", email="New_email",
                               email2="New_email_2", email3="New_email_3", homepage="New_homepage", bday='2', bmonth='February', byear='2001', aday='3', amonth='March', ayear='2011')
    modify_contact.id = old_contacts[index].id
    app.contact.modification_random_contact(modify_contact, index)
    new_contacts = app.contact.get_contact_list()
    # проверка по длине списка
    assert len(old_contacts) == len(new_contacts)
    # добавление в "старый" список модифицированного контакта
    old_contacts[index] = modify_contact
    # проверка по id, имени и фамилии
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)