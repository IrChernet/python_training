# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group1(app):
    app.group.create(Group(name="my1", header="hed1", footer="footer1"))


def test_add_group_empty(app):
    app.group.create(Group(name="", header="", footer=""))
