# -*- coding: utf-8 -*-
from models.contact import Contact

def test_modification_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modification()
    app.session.logout()