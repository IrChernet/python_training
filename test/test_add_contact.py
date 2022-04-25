# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", passw='secret')
    app.contact.create(Contact(first='FF', middle='MM', nick='NN', title='TT', address='AD', mobile='99',
                                            email='d@m.e'))
    app.session.logout()
