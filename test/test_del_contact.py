# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first='new F'))
    app.contact.delete_first()
