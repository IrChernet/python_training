# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    app.session.login(username="admin", passw="secret")
    app.group.edit_first(Group(name="new group"))
    app.session.logout()

def test_edit_group_header(app):
    app.session.login(username="admin", passw="secret")
    app.group.edit_first(Group(header="new head"))
    app.session.logout()

def test_edit_group_footer(app):
    app.session.login(username="admin", passw="secret")
    app.group.edit_first(Group(footer="new footer"))
    app.session.logout()