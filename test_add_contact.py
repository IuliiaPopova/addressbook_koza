import unittest

from selenium import webdriver

from contact import Contact


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.set_window_position(0, -1000)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_add_contact(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.add_new_cont()
        self.add_address()
        self.create_new_cont(Contact(first_name="Olga", last_name="Kozlova"))
        self.logout()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.driver.find_element_by_name("user").send_keys(username)
        self.driver.find_element_by_name("pass").send_keys(password)
        self.driver.find_element_by_xpath('//input[@type = "submit"]').click()

    def add_new_cont(self):
        self.driver.find_element_by_xpath('//a[@href  = "edit.php"]').click()

    def add_address(self):
        self.driver.find_element_by_xpath('//input[@name = "quickadd"][1]').click()



    def create_new_cont(self, contact):
        self.driver.find_element_by_name("firstname").send_keys(contact.first_name)
        self.driver.find_element_by_name("lastname").send_keys(contact.last_name)
        self.driver.find_element_by_name("submit").click()
    #
    def logout(self):
        self.driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
