# -*- coding: utf-8 -*-
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    contact_cache = None

    def open_page_new_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("mobile")) > 0):
            wd.find_element_by_link_text("add new").click()


    def open_page_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("MainForm")) > 0):
            wd.find_element_by_link_text("home").click()


    def select_first_contact(self):
        wd = self.app.wd
        self.open_page_home()
        wd.find_element_by_name("selected[]").click()


    def create(self, contact):
        wd = self.app.wd
        # open page contact
        self.open_page_new_contact()
        # go to add new
        wd.find_element_by_link_text("add new").click()
        # fill inputs
        self.fill_form_contact(contact)
        # submit
        self.submit_new_contact()
        # go to home page
        self.open_page_home()
        self.contact_cache = None

    def fill_form_contact(self, contact):
        wd = self.app.wd
        self.change_contact("firstname", contact.first)
        self.change_contact("middlename", contact.middle)
        self.change_contact("nickname", contact.nick)
        self.change_contact("title", contact.title)
        self.change_contact("address", contact.address)
        self.change_contact("mobile", contact.mobile)
        self.change_contact("email", contact.email)
        self.change_contact("lastname", contact.last)

    def delete_first(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit delete in modal window
        wd.switch_to.alert.accept()
        wd.find_element_by_name("searchstring")
        self.contact_cache = None


    def change_contact(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fild_name).click()
            wd.find_element_by_name(fild_name).clear()
            wd.find_element_by_name(fild_name).send_keys(text)

    def edit_first(self, new_contact_date):
        wd = self.app.wd
        self.select_first_contact()
        # img Edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill form
        self.fill_form_contact(new_contact_date)
        # submit edit
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_page_home()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_page_home()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                l_name = element.find_element_by_xpath("td[2]").text
                f_name = element.find_element_by_xpath("td[3]").text
                id_cont = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first=f_name, last=l_name, id=id_cont))
        return list(self.contact_cache)



