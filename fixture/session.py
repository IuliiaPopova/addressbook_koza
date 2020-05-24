"""
Login and logout
"""

class Session:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        """
        Login in the account
        :param username: username
        :param password: password
        """
        self.app.open_home_page()
        self.app.driver.find_element_by_name("user").click()
        self.app.driver.find_element_by_name("user").clear()
        self.app.driver.find_element_by_name("user").send_keys(username)
        self.app.driver.find_element_by_name("pass").click()
        self.app.driver.find_element_by_name("pass").clear()
        self.app.driver.find_element_by_name("pass").send_keys(password)
        self.app.driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        """
        Logout from the account
        """
        self.app.driver.find_element_by_name("logout").click()

    def ensure_logout(self):
        """
        Checking name of webelement "Logout" on the page, if it found we logout.
        """
        if self.app.driver.find_elements_by_name("logout"):
            self.logout()

    def correct_username(self, username):
        """
        Compare actual and expected username
        :param username: username
        :return:True or False
        """
        return self.app.driver.find_element_by_xpath('//*[@id="top"]/form/b').text == "(" + username + ")"

    def ensure_login(self, username, password):
        """
        Login in the account if username is correct else logout
        """
        if self.app.driver.find_elements_by_name("logout"):
            if self.correct_username(username):
                #If username is correct
                return
            else:
                #Logout if username is incorrect
                self.logout()
        self.login(username, password)
