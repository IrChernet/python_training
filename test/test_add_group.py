# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    # create fixture
    fixture = Application()
    # destroy fixture
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group1(app):
    app.session.login(username="admin", passw='secret')
    app.group.create(Group(name="my1", header="hed1", footer="footer1"))
    app.session.logout()


def test_add_group_empty(app):
    app.session.login(username="admin", passw='secret')
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
