# -*- coding: utf-8 -*-
from models.contact import Contact

def test_modification_contact(app):
    app.contact.modification(Contact(firstname="New_first_name", middlename="New_middle_name", lastname="New_last_name", nickname="New_nickname", title="New_title", company="New_company", address="New_address",
                               home="New_telephone_home", mobile="New_telephone_mobile", work="New_telephone_work", fax="New_telephone_fax", email="New_email",
                               email2="New_email_2", email3="New_email_3", homepage="New_homepage", bday='2', bmonth='February', byear='2001', aday='3', amonth='March', ayear='2011'))