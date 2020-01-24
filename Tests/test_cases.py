from selenium import webdriver
import unittest
from PageObjects.Basescreen import BaseScreen
from PageObjects.githubpage import Login
from Values import strings

class TestGitHubLogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(strings.url)


    def test_log_in(self):
        page = Login(self.driver)
        page.click_sign_in()
        page.enter_username(strings.username)
        page.enter_password(strings.password)
        page.click_login()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()







