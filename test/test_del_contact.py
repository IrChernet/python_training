# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_first_contact(app):
    app.contact.open_page_home()
    app.contact.delete_first()
