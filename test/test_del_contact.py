# -*- coding: utf-8 -*-

from model.contact import Contact

def test_del_first_contact(app):
    app.session.login(username="admin", passw='secret')
    app.contact.open_page_home()
    app.contact.delete_first()
    app.session.logout()