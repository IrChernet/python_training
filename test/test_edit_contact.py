# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_in_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(first='new test'))
    cont = Contact(first='new F')
    cont.id = old_contacts[0].id
    app.contact.edit_first(cont)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_middle_in_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first='new test'))
#    app.contact.edit_first(Contact(middle='new MM'))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

#def test_edit_last_in_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first='new test'))
#    app.contact.edit_first(Contact(last="New last"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)



