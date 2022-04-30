# -*- coding: utf-8 -*-

def test_edit_group(app):
    app.session.login(username="admin", passw="secret")
    app.group.edit_group()
    app.session.logout()