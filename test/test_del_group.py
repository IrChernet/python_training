# -*- coding: utf-8 -*-

def test_del_1group(app):
    app.group.delete_1group()
    app.session.logout()