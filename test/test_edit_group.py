# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    group = Group(name="new group")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test group"))
#    group = Group(header="new head")
#    app.group.edit_first(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

# def test_edit_group_footer(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="test group"))
#    group = Group(footer="new footer")
#    app.group.edit_first(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
