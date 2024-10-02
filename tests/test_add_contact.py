# -*- coding: utf-8 -*-
from models.contact import Contact

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="First_name", middlename="Middle_name", lastname="Last_name", nickname="Nickname", title="Title", company="Company", address="Address",
                               home="Telephone_home", mobile="Telephone_mobile", work="Telephone_work", fax="Telephone_fax", email="email",
                               email2="email_2", email3="email_3", homepage="homepage", bday='1', bmonth='January', byear='2000', aday='2', amonth='February', ayear='2010'))
    app.session.logout()