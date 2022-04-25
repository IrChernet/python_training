# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.appl1 import Appgroup


@pytest.fixture
def appgr(request):
    # create fixture
    fixture = Appgroup()
    # destroy fixture
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_empty_group(appgr):
    appgr.login(username="admin", passw='secret')
    appgr.create_group(Group(name="", header="", footer=""))
    appgr.logout()


def test_add_group1(appgr):
    appgr.login(username="admin", passw='secret')
    appgr.create_group(Group(name="my1", header="hed1", footer="footer1"))
    appgr.logout()