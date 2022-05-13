# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):

    if app.contact.count() == 0:
        app.contact.create(Contact(first='new test'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    cont = Contact(first='FF test-1')
    cont.id = old_contacts[index].id
    print(index)
    app.contact.edit_by_index(cont, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_middle_in_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first='new test'))
#    app.contact.edit_first(Contact(middle='new MM'))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

# def test_edit_last_in_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    if app.contact.count() == 0:
#        app.contact.create(Contact(first='new test'))
#    app.contact.edit_first(Contact(last="New last"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
