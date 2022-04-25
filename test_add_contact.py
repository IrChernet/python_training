# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from appl2 import AppContact


@pytest.fixture
def app(request):
    fixture = AppContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", passw='secret')
    app.create_contact(Contact(first='FF', middle='MM', nick='NN', title='TT', address='AD', mobile='99',
                                            email='d@m.e'))
    app.logout()
