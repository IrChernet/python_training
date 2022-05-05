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
        self.fill_form_group(group)
        # submit
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_form_group(self, group):
        wd = self.app.wd
        self.change("group_name", group.name)
        self.change("group_header", group.header)
        self.change("group_footer", group.footer)


    def change(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fild_name).click()
            wd.find_element_by_name(fild_name).clear()
            wd.find_element_by_name(fild_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first(self, new_group_date):
        wd = self.app.wd
        self.open_group_page()
        # select 1 group
        self.select_first_group()
        # go edit
        wd.find_element_by_name("edit").click()
        # new elements
        self.fill_form_group(new_group_date)
        # submit changes
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))





