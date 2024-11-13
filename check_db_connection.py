import pymysql.cursors
from fixtures.db import DbFixture
from fixtures.orm import ORMFixture
from models.group import Group

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    l = db.get_contacts_not_in_group(Group(id='367'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass