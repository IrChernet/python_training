# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first='FF', middle='MM', nick='NN', title='TT', address='AD',
                                            email='d@m.e'))
    app.contact.create(Contact(first='ФА', middle='Иванов', address='Иванов адрес',
                                            email='i@m.e'))
    app.contact.create(Contact(first=' ', middle='MM', email='ht@m.e'))
