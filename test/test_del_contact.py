# -*- coding: utf-8 -*-

from model.contact import Contact

def test_del_1contact(app):
    app.session.login(username="admin", passw='secret')
    app.contact.delete1Contact()
    app.session.logout()