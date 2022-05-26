# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_full_string(prefix, maxlen):
    sumbol = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(sumbol) for i in range(random.randrange(maxlen))])


def random_phone_string(prefix, maxlen):
    sumbol = "+" + string.digits + "-"
    return prefix + "".join([random.choice(sumbol) for i in range(random.randrange(maxlen))])


def random_mail_string(prefix, maxlen):
    sumbol = string.ascii_letters + "@" + string.digits
    return prefix + "".join([random.choice(sumbol) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(first=first, last="last", address="address", email="email", mobile="mobile", home="home")
    for first in ["", random_full_string("first", 10)]
#    for last in ["", random_full_string("last", 15)]
#   for address in ["", random_full_string("address", 30)]
#    for email in ["", random_mail_string("email", 15)]
#    for mobile in ["", random_phone_string("mobile", 10)]
#    for home in ["", random_phone_string("home", 10)]
]


@pytest.mark.parametrize("cont", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, cont):
    print("test  ")
    app.contact.open_page_home()
    old_contacts = app.contact.get_contact_list()
    print("print list contacts ", old_contacts)
    app.contact.create(cont)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
