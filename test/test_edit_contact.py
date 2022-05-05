# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_in_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first='new test'))
    app.contact.edit_first(Contact(first='new F'))

def test_edit_middle_in_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first='new test'))
    app.contact.edit_first(Contact(middle='new MM'))

def test_edit_last_in_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first='new test'))
    app.contact.edit_first(Contact(last="New last"))

