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
            cursor.execute('select id, lastname, firstname, address, email, email2, email3, home, mobile, work from addressbook')
            for row in cursor:
                (id, lastname, firstname, address, email, email2, email3, home, mobile, work) = row
                list.append(Contact(id=str(id), lastname=lastname, firstname=firstname, address=address, email=email, email2=email2, email3=email3, home=home, mobile=mobile, work=work))
        finally:
            cursor.close()
        return list

    # получение контакта, который не состоит в группе
    def get_contact_without_group(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('select a.id from addressbook a left join address_in_groups b on a.id = b.id where b.id is null')
            id_contact = cursor.fetchone()[0]
        finally:
            cursor.close()
        return id_contact

    # получение количества записей для определенного контакта с определенной группой
    def get_contact_by_group_id(self, id_contact, id_group):
        cursor = self.connection.cursor()
        try:
            cursor.execute('select count(*) from address_in_groups where group_id = "%s" and id = "%s"' % (id_group, id_contact))
            count = cursor.fetchone()[0]
        finally:
            cursor.close()
        return count

    # получение информации о пользователе по id
    def get_info_about_contact_by_id(self, id_contact):
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, lastname, firstname, address, email, email2, email3, home, mobile, work from addressbook where id = "%s"' % id_contact)
            for row in cursor:
                (id, lastname, firstname, address, email, email2, email3, home, mobile, work) = row
                contact = Contact(id=str(id), lastname=lastname, firstname=firstname, address=address, email=email,
                                    email2=email2, email3=email3, home=home, mobile=mobile, work=work)
        finally:
            cursor.close()
        return contact

    # получение списка id контактов из БД
    def get_id_contact_list(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id from addressbook')
            list = cursor.fetchall()
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()