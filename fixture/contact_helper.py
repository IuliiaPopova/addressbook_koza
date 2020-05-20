class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new_cont(self):
        self.app.driver.find_element_by_xpath('//a[@href  = "edit.php"]').click()

    def add_address(self):
        self.app.driver.find_element_by_xpath('//input[@name = "quickadd"][1]').click()

    def create(self, contact):
        self.add_new_cont()
        self.add_address()
        self.app.driver.find_element_by_name("firstname").send_keys(contact.first_name)
        self.app.driver.find_element_by_name("lastname").send_keys(contact.last_name)
        self.app.driver.find_element_by_name("submit").click()
