# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first='new test'))
    app.contact.edit_first(Contact(first='new F'))
    app.contact.edit_first(Contact(middle='new MM'))
    app.contact.edit_first(Contact(last="New last"))
