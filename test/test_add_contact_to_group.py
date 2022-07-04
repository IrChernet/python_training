from model.group import Group
from model.contact import Contact
from random import randrange
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_get_contacts_in_groups():
    try:
        l = db.get_contact_in_group(Group(id="140"))
        for item in l:
            print(len(l))
        pass
    finally:
        pass
    pass


def test_add_some_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first='new F'))
    app.contact.open_page_home()
    list_contacts = db.get_contact_list()
    list_groups = db.get_group_list()
    ind_cont = randrange(len(list_contacts))
    ind_gr = randrange(len(list_groups))
    app.contact.select_contact_by_index(ind_cont)
    app.contact.add_to_group(ind_cont, ind_gr)

