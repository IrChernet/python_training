# -*- coding: utf-8 -*-

def test_del_1group(app):
    app.session.login(username="admin", passw="secret")
    app.group.delete_1group()
    app.session.logout()