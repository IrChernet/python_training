from model.contact import Contact
import re
from random import randrange


def test_some_contact_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_homepage = app.contact.get_contact_info_by_index(index)
    contact_info_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.first == contact_info_from_edit_page.first
    assert contact_from_homepage.last == contact_info_from_edit_page.last
    assert contact_from_homepage.address == contact_info_from_edit_page.address
    assert contact_from_homepage.all_phones == merge_phones(contact_info_from_edit_page)
    assert contact_from_homepage.all_mails == merge_mails(contact_info_from_edit_page)


def test_all_contacts_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first='new F'))
    contacts_list_db = db.get_contact_list()
    contact_from_homepage = app.contact.get_contact_list()
    assert sorted(contact_from_homepage, key=Contact.id_or_max) == sorted(contacts_list_db, key=Contact.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.home, contact.mobile, contact.work, contact.secondphone]))))


def merge_mails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3])))