"""
Group behavior: methods , etc.
"""
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        """
        Open group page if we are not located on group page now.
        """
        if not (self.app.driver.current_url.endswith("/group.php") and self.app.driver.find_elements_by_name("new")):
            self.app.driver.find_element_by_link_text("groups").click()

    def create(self, group):
        """
        Create new group
        :param group:group
        """
        self.open_group_page()
        self.app.driver.find_element_by_name("new").click()
        self.fill(group)
        self.app.driver.find_element_by_name("submit").click()
        self.open_group_page()
        self.group_cache = None

    def modify(self, group):
        """
        Modify selected group
        :param group: group
        """
        self.open_group_page()
        self.select_first_group()
        self.app.driver.find_element_by_name("edit").click()
        self.fill(group)
        self.app.driver.find_element_by_name("update").click()
        self.open_group_page()
        self.group_cache = None

    def delete(self):
        """
        Delete selected group
        """
        self.open_group_page()
        self.select_first_group()
        self.app.driver.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def select_first_group(self):
        """
        Select first group

        """
        self.app.driver.find_element_by_xpath('//input[@name = "selected[]"]').click()

    def change_field_value(self, field_name, text):
        """
        Checking text: if text ==None , break, else fill value
        :param field_name:attribute "name" in the Web element
        :param text: text
        :return:
        """
        if text is not None:
            self.app.driver.find_element_by_name(field_name).click()
            self.app.driver.find_element_by_name(field_name).clear()
            self.app.driver.find_element_by_name(field_name).send_keys(text)

    def fill(self, group):
        """
        fill group form
        :param group: group. Parameters name, header, footer are retrieved from object of group

        """
        self.change_field_value(field_name="group_name", text=group.name)
        self.change_field_value(field_name="group_header", text=group.header)
        self.change_field_value(field_name="group_footer", text=group.footer)

    def count(self):
        """
        Determine amount of the current groups
        :return: amount of groups on the page
        """
        self.open_group_page()
        return len(self.app.driver.find_elements_by_xpath('//input[@name = "selected[]"]'))

    group_cache = None

    def get_groups_list(self):
        """
        Get groups
        :return:
        """
        if self.group_cache is None:

            self.open_group_page()
            self.group_cache = []
            groups = self.app.driver.find_elements_by_xpath('//input[@name="selected[]"]')
            for element in groups:
                name = element.get_attribute("title")
                id = element.get_attribute("value")
                self.group_cache.append(Group(name=name[8:-1], id=id))
        return list(self.group_cache)# return copy of cache using list

