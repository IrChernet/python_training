# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group1(app):
    old_groups = app.group.get_group_list
    app.group.create(Group(name="my1", header="hed1", footer="footer1"))
    new_groups = app.group.get_group_list
    assert len(old_groups) + 1 == len(new_groups)


#def test_add_group_empty(app):
#    app.group.create(Group(name="", header="", footer=""))
