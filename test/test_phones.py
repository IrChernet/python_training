
# from model.contact import Contact
import re

def test_phones_on_home_page(app):
    first_contact_from_homepage = app.contact.get_contact_list()[0]
    first_contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert first_contact_from_homepage.all_phones == merge_phones(first_contact_from_editpage)


def test_phones_on_view_page(app):
    first_contact_from_viewpage = app.contact.get_contact_from_viewpage(0)
    first_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert merge_phones(first_contact_from_viewpage) == merge_phones(first_contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.home, contact.mobile, contact.work, contact.secondphone]))))

