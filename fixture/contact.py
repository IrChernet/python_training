# -*- coding: utf-8 -*-
class ContactHelper:

    def __init__(self, app):
        self.app = app


    def submit_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()


    def open_page_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def open_page_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def create(self, contact):
        wd = self.app.wd
        # open page contact
        self.open_page_contact()
        # go to add new
        wd.find_element_by_link_text("add new").click()
        # fill inputs
        wd.find_element_by_name("firstname").send_keys(contact.first)
        wd.find_element_by_name("middlename").send_keys(contact.middle)
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit
        self.submit_new_contact()
        # go to home page
        self.open_page_home()
