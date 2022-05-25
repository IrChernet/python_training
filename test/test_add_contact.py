# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    cont = Contact(first='FF2', last='ksds', middle='MM1', nick='NN1', title='TT', address='AD', email='d+1@m.e',
                   mobile='12(1)21', home='+3(3)333')
#                   workphone='009988', fax='098765'
    app.contact.create(cont)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
