from selenium.webdriver.common.by import By
from Values import strings
from .Basescreen import BaseScreen

class Login(BaseScreen):

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_xpath = "//a[@class='HeaderMenu-link no-underline mr-3']"
        self.username_textbox_id = "login_field"
        self.password_textbox_id = "password"
        self.sign_in_button_name = "commit"

    def click_sign_in(self,):
        self.driver.find_element_by_xpath(self.sign_in_xpath).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.sign_in_button_name).click()


