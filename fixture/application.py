"""
Class Application:
1. Create instance of class Webdriver
2. Access to browser
3. Access to all internal classes
"""

from selenium import webdriver

from fixture.contact import Contact
from fixture.group import GroupHelper
from fixture.session import Session


class Application(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.set_window_position(0, -1000)#open browser in window position with a given value
        self.driver.maximize_window() #open browser on the fullscreen
        self.driver.implicitly_wait(1)#the driver should wait when searching for an element
        self.session = Session(self)#create instance of the class Session
        self.group = GroupHelper(self)#create instance of the class Group
        self.contact = Contact(self)#create instance of the class Contact

    def is_valid(self):
        try:
            x = self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")#open to home page

    def tear_down(self):
        self.driver.quit()#browser is closed
