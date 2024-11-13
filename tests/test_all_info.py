import re
from models.contact import Contact


# проверка, что информация о контактах на домашней странице соответствует данным в БД (сравнение для всех записей)
def test_all_info_with_db(app, db):
    list = db.get_id_contact_list() # получение списка id контактов
    for element in list:
        id_contact = element[0]
        contact_from_home_page = app.contact.get_info_about_contact_by_id(id_contact)
        contact_from_db = db.get_info_about_contact_by_id(id_contact)
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)

# проверка, что информация о контакте на домашней странице соответствуют данным в карточке редактирования контакта
#def test_phones_on_home_page(app):
    #contact_from_home_page = app.contact.get_contact_list()[0]
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    #assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    #assert contact_from_home_page.address == contact_from_edit_page.address
    #assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    #assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

# чистка строки от лишних символов
def clear(s):
    return re.sub('[() -]', '', s)

# "склеивание" телефонов
def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))

# "склеивание" email
def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))