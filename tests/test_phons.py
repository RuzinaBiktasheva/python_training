import re

# проверка, что номера телефонов на домашней странице соответствуют данным в карточке редактирования контакта
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home == clear(contact_from_edit_page.home)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.work == clear(contact_from_edit_page.work)

# проверка, что номера телефонов на странице просмотра соответствуют данным в карточке редактирования контакта
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work

# чистка строки от лишних символов
def clear(s):
    return re.sub('[() -]', '', s)