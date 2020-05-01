import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Elearning_Test2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://skanak.pythonanywhere.com/")
        signup = driver.find_element_by_xpath('//*[@id="mainMenu"]/ul/li/form/a[2]').click()
        time.sleep(3)
        signup_username = driver.find_element_by_xpath('//*[@id="id_username"]')
        signup_username.send_keys("testuser5")
        signup_pwd = driver.find_element_by_xpath('//*[@id="id_password1"]')
        signup_pwd.send_keys("test4321")
        signup_confirm_pwd = driver.find_element_by_xpath('//*[@id="id_password2"]')
        signup_confirm_pwd.send_keys("test4321")
        time.sleep(3.0)
        register = driver.find_element_by_xpath('/html/body/div/div/form/button').click()
        time.sleep(3.0)
        try:
            # attempt to find the plus button - if found, logged in
            logout = driver.find_element_by_xpath('//*[@id="mainMenu"]/ul/li/p/a[2]')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()