# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.open_page_home()
    app.contact.edit_first(Contact(first='new F', middle='MM', last="New last", nick='NN', title='TT', address='AD', mobile='99',
                                            email='d@m.e'))
