import pymysql.cursors
from models.group import Group
from models.contact import Contact

class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    # получение списка групп из БД
    def get_group_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    # получение списка контактов из БД
    def get_contact_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute('select id, lastname, firstname, address from addressbook')
            for row in cursor:
                (id, lastname, firstname, address) = row
                list.append(Contact(id=str(id), lastname=lastname, firstname=firstname, address=address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()