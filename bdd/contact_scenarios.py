from pytest_bdd import scenario
from .contact_steps import *

@scenario('contacts.feature', 'Add new contact')
def test_add_new_contact():
    pass

@scenario('contacts.feature', 'Delete contact')
def test_delete_contact():
    pass

@scenario('contacts.feature', 'Modification contact')
def test_modification_contact():
    pass