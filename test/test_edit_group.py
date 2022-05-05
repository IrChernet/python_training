# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    app.group.edit_first(Group(name="new group"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    app.group.edit_first(Group(header="new head"))


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    app.group.edit_first(Group(footer="new footer"))
