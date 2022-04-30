# -*- coding: utf-8 -*-

def test_edit_contact(app):
    app.session.login(username="admin", passw="secret")
    app.contact.edit()
    app.session.logout()