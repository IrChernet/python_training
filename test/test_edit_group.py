# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    app.group.edit_first(Group(name="new group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    app.group.edit_first(Group(header="new head"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_footer(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    app.group.edit_first(Group(footer="new footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
