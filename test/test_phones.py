
# from model.contact import Contact
import re

def test_phones_on_home_page(app):
    first_contact_from_homepage = app.contact.get_contact_list()[0]
    first_contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert first_contact_from_homepage.home == clear(first_contact_from_editpage.home)
    assert first_contact_from_homepage.work == clear(first_contact_from_editpage.work)
    assert first_contact_from_homepage.mobile == clear(first_contact_from_editpage.mobile)
#   assert first_contact_from_homepage.fax == first_contact_from_edit_page.fax

def test_phones_on_view_page(app):
    first_contact_from_viewpage = app.contact.get_contact_from_viewpage(0)
    first_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert first_contact_from_viewpage.home == first_contact_from_edit_page.home
    assert first_contact_from_viewpage.work == first_contact_from_edit_page.work
    assert first_contact_from_viewpage.mobile == first_contact_from_edit_page.mobile
    assert first_contact_from_viewpage.fax == first_contact_from_edit_page.fax

def clear(s):
    return re.sub("[() -]", "", s)
