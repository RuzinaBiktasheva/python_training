from models.contact import Contact
from models.group import Group
import random


# тест на добавление контакта в группу
def test_add_contact_to_group(app, db):
    # предусловия
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First_name_contact_for_added"))
    if app.group.count() == 0:
        app.group.create(Group(name="Name_group_for_added"))
    # получение списка контактов из БД
    contacts = db.get_contact_list()
    # произвольный пользователь
    used_contact = random.choice(contacts)
    # получение списка групп из БД
    groups = db.get_group_list()
    # произвольная группа
    used_group = random.choice(groups)
    # id контакта и группы
    id_contact = used_contact.id
    id_group = used_group.id
    # добавление контакта в группу
    app.contact.add_contact_to_group(id_contact, id_group)
    # проверка, что у контакта добавилась группа в БД
    assert db.get_contact_by_group_id(id_contact, id_group) == 1