# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

from group import Group


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.set_window_position(0, -1000)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_add_group(self):
        self.login(username="admin", password="secret")
        group = Group(name="dfgdfg", header="dfgdfg", footer="dfgfghgfhg")
        self.create_group(group)
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element_by_name("user").click()
        self.driver.find_element_by_name("user").clear()
        self.driver.find_element_by_name("user").send_keys(username)
        self.driver.find_element_by_name("pass").click()
        self.driver.find_element_by_name("pass").clear()
        self.driver.find_element_by_name("pass").send_keys(password)
        self.driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_group_page(self):
        self.driver.find_element_by_link_text("groups").click()

    def create_group(self, group):
        self.open_group_page()
        self.driver.find_element_by_name("new").click()
        self.driver.find_element_by_name("group_name").click()
        self.driver.find_element_by_name("group_name").clear()
        self.driver.find_element_by_name("group_name").send_keys(group.name)
        self.driver.find_element_by_name("group_header").click()
        self.driver.find_element_by_name("group_header").clear()
        self.driver.find_element_by_name("group_header").send_keys(group.header)
        self.driver.find_element_by_name("group_footer").click()
        self.driver.find_element_by_name("group_footer").clear()
        self.driver.find_element_by_name("group_footer").send_keys(group.footer)
        self.driver.find_element_by_name("submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        # return to group page
        self.driver.find_element_by_link_text("group page").click()

    def logout(self):
        # logout
        self.driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
