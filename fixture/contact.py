"""
Contact behavior: methods , etc.
"""

class Contact:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        """
        Create new contact
        :param contact: contact
        """
        self.add_new_cont()
        self.add_address()
        self.fill(contact)
        self.app.driver.find_element_by_name("submit").click()
        self.open_contact_page()

    def modify(self, contact):
        """
        Modify selected contact
        :param contact: contact
        """
        self.open_contact_page()
        self.select_first_contact()
        self.app.driver.find_element_by_css_selector("img[alt='Edit']").click()
        self.fill(contact)
        self.app.driver.find_element_by_name('update').click()
        self.open_contact_page()

    def add_new_cont(self):
        """
        Button "Add new" for go to contact page
        """
        self.app.driver.find_element_by_xpath('//a[@href  = "edit.php"]').click()

    def add_address(self):
        """
        Button "Next" in Edit/add address book entry
        """
        self.app.driver.find_element_by_xpath('//input[@name = "quickadd"][1]').click()

    def open_contact_page(self):
        """
        Open contact page/refresh
        """
        self.app.driver.find_element_by_xpath('//*[contains(text(), "home")]').click()

    def select_first_contact(self):
        """Select of the contact"""
        self.app.driver.find_element_by_xpath('//input[@name="selected[]"]').click()

    def fill(self, contact):
        """
        fill contact form
        :param contact: contact
        """
        self.change_field_value(xpath='//input[@name="firstname"]', text=contact.first_name)
        self.change_field_value(xpath='//input[@name="lastname"]', text=contact.last_name)

    def delete(self):
        """
        Delete selected contact
        """
        self.app.driver.find_element_by_xpath('//a[@href="./"]').click()
        self.select_first_contact()
        self.app.driver.find_element_by_xpath('//input[@value="Delete"]').click()
        self.app.driver.switch_to_alert().accept()
        self.open_contact_page()

    # common method
    def change_field_value(self, xpath: str, text: str):
        """
        Checking text: if text ==None , break, else fill value

        """
        if text is not None:
            self.app.driver.find_element_by_xpath(xpath).click()
            self.app.driver.find_element_by_xpath(xpath).clear()
            self.app.driver.find_element_by_xpath(xpath).send_keys(text)
