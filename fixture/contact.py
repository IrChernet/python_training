# -*- coding: utf-8 -*-
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    contact_cache = None
    c_id = None

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
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_page_home()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id_cont):
        wd = self.app.wd
        self.open_page_home()
        wd.find_element_by_css_selector("input[value='%s']" % id_cont).click()

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
        self.change_contact("home", contact.home)
        self.change_contact("work", contact.work)
        self.change_contact("fax", contact.fax)
        self.change_contact("email", contact.email)
        self.change_contact("email2", contact.email2)
        self.change_contact("email3", contact.email3)
        self.change_contact("lastname", contact.last)

    def delete_first(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit delete in modal window
        wd.switch_to.alert.accept()
        wd.find_element_by_name("searchstring")
        self.contact_cache = None

    def delete_contact_by_id(self, id_cont):
        wd = self.app.wd
        self.select_contact_by_id(id_cont)
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
        self.edit_by_index(new_contact_date, 0)

    def edit_by_index(self, new_contact_date, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # img Edit
        s = "//*[@id='maintable']//tr[" + str(index+2) + "]/td[8]"
        # fill form
        wd.find_element_by_xpath(s).click()
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
            for element in wd.find_elements_by_name("entry"):
                l_name = element.find_element_by_xpath("td[2]").text
                f_name = element.find_element_by_xpath("td[3]").text
                all_phones = element.find_element_by_xpath("td[6]").text
                all_mails = element.find_element_by_xpath("td[5]").text
                address = element.find_element_by_xpath("td[4]").text
                id_cont = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(
                    Contact(id_cont=id_cont, first=f_name, last=l_name, all_phones=all_phones,
                            address=address, all_mails=all_mails))
        return list(self.contact_cache)

    def get_contact_info_by_index(self, index):
        wd = self.app.wd
        s = "//*[@id='maintable']//tr["+ str(index + 2)
        s2 = s + "]/td[2]"
        s3 = s + "]/td[3]"
        s4 = s + "]/td[4]"
        s5 = s + "]/td[5]"
        s6 = s + "]/td[6]"
        l_name = wd.find_element_by_xpath(s2).text
        f_name = wd.find_element_by_xpath(s3).text
        all_phones = wd.find_element_by_xpath(s6).text
        all_mails = wd.find_element_by_xpath(s5).text
        address = wd.find_element_by_xpath(s4).text
        id_cont = wd.find_element_by_name("selected[]").get_attribute("value")
        return Contact(id_cont=id_cont, first=f_name, last=l_name, all_phones=all_phones,
                            address=address, all_mails=all_mails)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_page_home()
        self.select_contact_by_index(index)
        s = "//*[@id='maintable']//tr[" + str(index + 2) + "]/td[8]"
        wd.find_element_by_xpath(s).click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_page_home()
        self.select_contact_by_index(index)
        s = "//*[@id='maintable']//tr[" + str(index + 2) + "]/td[7]"
        wd.find_element_by_xpath(s).click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id_cont = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").text
        return Contact(first=firstname, last=lastname, id_cont=id_cont,
                       home=home, mobile=mobile, work=work,  secondphone=secondphone,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_from_viewpage(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_xpath("//div[@id='content']").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        secondphone = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, secondphone=secondphone)
