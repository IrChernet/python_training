# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group1(app):
    app.session.login(username="admin", passw='secret')
    app.group.create(Group(name="my1", header="hed1", footer="footer1"))
    app.session.logout()


def test_add_group_empty(app):
    app.session.login(username="admin", passw='secret')
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
