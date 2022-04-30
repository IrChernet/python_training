# -*- coding: utf-8 -*-
class SessionHelper:

    def __init__(self, app):
        self.app = app


    def open_home_page(self):
        wd = self.app.wd
        # open home page
        wd.get("http://localhost/addressbook/")


    def login(self, username, passw):
        wd = self.app.wd
        # open home page
        self.open_home_page()
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(passw)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")
