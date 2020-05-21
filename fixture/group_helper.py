class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        self.app.driver.find_element_by_link_text("groups").click()

    def create(self, group):
        self.open_group_page()
        self.app.driver.find_element_by_name("new").click()
        self.app.driver.find_element_by_name("group_name").click()
        self.app.driver.find_element_by_name("group_name").clear()
        self.app.driver.find_element_by_name("group_name").send_keys(group.name)
        self.app.driver.find_element_by_name("group_header").click()
        self.app.driver.find_element_by_name("group_header").clear()
        self.app.driver.find_element_by_name("group_header").send_keys(group.header)
        self.app.driver.find_element_by_name("group_footer").click()
        self.app.driver.find_element_by_name("group_footer").clear()
        self.app.driver.find_element_by_name("group_footer").send_keys(group.footer)
        self.app.driver.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete(self):
        self.open_group_page()
        self.app.driver.find_element_by_xpath('//input[@name = "selected[]"][1]').click()
        self.app.driver.find_element_by_name("delete").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        self.app.driver.find_element_by_link_text("group page").click()
