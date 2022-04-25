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


def test_del_1group(app):
    app.group.delete_1group()
    app.session.logout()