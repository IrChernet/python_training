# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.open_page_home()
    app.contact.edit_first(Contact(first='new F'))
    app.contact.edit_first(Contact(middle='new MM'))
    app.contact.edit_first(Contact(last="New last"))
