from models.contact import Contact
from pytest_bdd import given, when, then, parsers
import random

# добавление нового контакта
@given("a contact list", target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()

@given(parsers.parse('a contact with {lastname}, {firstname} and {address}'), target_fixture='new_contact')
def new_contact(lastname, firstname, address):
    return Contact(lastname=lastname, firstname=firstname, address=address)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# удаление случайного контакта
@given("a contact list", target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()

@given('random contact', target_fixture='random_contact')
def random_contact(contact_list):
    return random.choice(contact_list)

@when('I delete the contact to the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old list with the deleted contact')
def verify_contact_deleted(db, contact_list, random_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# модификация случайного контакта
@given("a contact list", target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()

@given('random contact', target_fixture='random_contact')
def random_contact(contact_list):
    return random.choice(contact_list)

@when(parsers.parse('I modification the contact to the list with {lastname}, {firstname} and {address}'))
def modification_contact(app, random_contact, lastname, firstname, address):
    modify_contact = Contact(lastname=lastname, firstname=firstname, address=address)
    app.contact.modification_contact_by_id(modify_contact, random_contact.id)

@then('the new contact list is equal to the old list with the modification contact')
def verify_contact_modification(db, contact_list, random_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(random_contact)] = random_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)