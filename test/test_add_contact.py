# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, data_contacts):
    cont = data_contacts
    app.contact.open_page_home()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(cont)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_json(app, json_contacts):
    cont = json_contacts
    app.contact.open_page_home()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(cont)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)