import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Elearning_test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://skanak.pythonanywhere.com/")
        login = driver.find_element_by_xpath('//*[@id="mainMenu"]/ul/li/form/a[1]').click()
        time.sleep(0.5)
        login_username = driver.find_element_by_xpath('//*[@id="id_username"]')
        login_username.send_keys("testuser1")
        login_pwd = driver.find_element_by_xpath("/html/body/div/div/div/div/form/p[2]/input")
        login_pwd.send_keys("test4321")
        time.sleep(0.5)
        login = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div/input').click()
        time.sleep(0.5)
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