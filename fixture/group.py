# -*- coding: utf-8 -*-
class GroupHelper:

    def __init__(self, app):
        self.app = app


    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        #init group greation
        wd.find_element_by_name("new").click()
        # fill form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_1group(self):
        wd = self.app.wd
        self.open_group_page()
        # select 1 group
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_group(self):
        wd = self.app.wd
        self.open_group_page()
        # select 1 group
        wd.find_element_by_name("selected[]").click()
        # submit edit
        wd.find_element_by_name("edit").click()
        # new elements
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("New n")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("new h")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("new f")
        # submit changes
        wd.find_element_by_name("update").click()
        self.return_to_group_page()




