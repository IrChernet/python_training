# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", passw='secret')
    app.contact.create(Contact(first='FF', middle='MM', nick='NN', title='TT', address='AD', mobile='99',
                                            email='d@m.e'))
    app.session.logout()
