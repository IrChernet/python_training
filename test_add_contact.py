# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(160)

    def login(self, wd, username, passw):
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(passw)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def submit_new_contact(self, wd):
        wd.find_element_by_name("submit").click()

    def open_page_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def open_page_home(self, wd):
        wd.find_element_by_link_text("home").click()

    def fill_form_contact(self, wd, contact):
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
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", passw='secret')
        self.open_page_contact(wd)
        self.fill_form_contact(wd, Contact(first='FF', middle='MM', nick='NN', title='TT', address='AD', mobile='99',
                                           email='d@m.e'))
        self.submit_new_contact(wd)
        self.open_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

if __name__ == "__main__":
    unittest.main()
