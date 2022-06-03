# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_del_some_contact(app, db, check_ui):

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first='new F'))
    old_contacts = db.get_contact_list()
    cont = random.choice(old_contacts)
    app.contact.delete_contact_by_id(cont.id_cont)
#    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(cont)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

