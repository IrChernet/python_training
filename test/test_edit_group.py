# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    app.group.edit_first(Group(name="new group"))


def test_edit_group_header(app):
    app.group.edit_first(Group(header="new head"))


def test_edit_group_footer(app):
    app.group.edit_first(Group(footer="new footer"))
