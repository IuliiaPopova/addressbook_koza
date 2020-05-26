"""
Contact behavior: methods , etc.
"""
from model.contact import Contact


class ContactHelper:
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
        self.contact_cache = None

    def modify(self, index, contact):
        """
        Modify selected contact
        :param contact: contact
        """
        self.open_contact_page()
        self.goto_edit_page(index)
        self.fill(contact)
        self.app.driver.find_element_by_name('update').click()
        self.open_contact_page()
        self.contact_cache = None

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

    def goto_edit_page(self, index):
        self.app.driver.find_elements_by_xpath('//img[@alt="Edit"]')[index].click()

    def open_contact_page(self):
        """
        Open contact page/refresh
        """
        if not self.app.driver.current_url.endswith("addressbook/"):
            self.app.driver.find_element_by_xpath('//*[contains(text(), "home")]').click()

    def select_contact(self,index):
        """Select of the contact"""
        self.app.driver.find_elements_by_xpath('//input[@name="selected[]"]')[index].click()

    def fill(self, contact):
        """
        fill contact form
        :param contact: contact
        """
        self.change_field_value(xpath='//input[@name="firstname"]', text=contact.first_name)
        self.change_field_value(xpath='//input[@name="lastname"]', text=contact.last_name)

    def delete(self,index):
        """
        Delete selected contact
        """
        self.open_contact_page()
        self.select_contact(index)
        self.app.driver.find_element_by_xpath('//input[@value="Delete"]').click()
        self.app.driver.switch_to_alert().accept()
        self.open_contact_page()
        self.contact_cache = None

    # common method
    def change_field_value(self, xpath: str, text: str):
        """
        Checking text: if text ==None , break, else fill value

        """
        if text is not None:
            self.app.driver.find_element_by_xpath(xpath).click()
            self.app.driver.find_element_by_xpath(xpath).clear()
            self.app.driver.find_element_by_xpath(xpath).send_keys(text)

    contact_cache = None

    def count(self):
        self.open_contact_page()
        return len(self.app.driver.find_elements_by_xpath('//input[@name = "selected[]"]'))

    def get_contact_list(self):
        """
        Get groups
        :return:
        """
        if self.contact_cache is None:

            self.open_contact_page()
            self.contact_cache = []
            contacts = self.app.driver.find_elements_by_xpath('//input[@name="selected[]"]')
            for element in contacts:
                name = element.get_attribute("title")[8:-1]
                first_name = name.split()[0]
                last_name = name.split()[1]
                id = element.get_attribute("value")
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id))
        return list(self.contact_cache)  # return copy of cache using list
