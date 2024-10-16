# -*- coding: utf-8 -*-
from models.contact import Contact

    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    added_contact = Contact(firstname="First_name", middlename="Middle_name", lastname="Last_name", nickname="Nickname", title="Title", company="Company", address="Address",
                               home="Telephone_home", mobile="Telephone_mobile", work="Telephone_work", fax="Telephone_fax", email="email",
                               email2="email_2", email3="email_3", homepage="homepage", bday='1', bmonth='January', byear='2000', aday='2', amonth='February', ayear='2010')
    app.contact.create(added_contact)
    new_contacts = app.contact.get_contact_list()
    # проверка по длине списка
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(added_contact)
    # проверка по id, имени и фамилии
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)