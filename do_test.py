import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Elearning_test4(unittest.TestCase):

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
        time.sleep(2)
        course = driver.find_element_by_xpath('/html/body/div/div/div/div/ol/li[1]/a').click()
        time.sleep(2)
        section = driver.find_element_by_xpath('/html/body/div/div/div/div/ul/li[1]/a').click()
        time.sleep(2)
        question_1 = driver.find_element_by_xpath('/html/body/div/form/ul[1]/li[2]/input').click()
        question_2 = driver.find_element_by_xpath('/html/body/div/form/ul[2]/li[4]/input').click()
        question_3 = driver.find_element_by_xpath('/html/body/div/form/ul[3]/li[4]/input').click()
        question_4 = driver.find_element_by_xpath('/html/body/div/form/ul[4]/li[1]/input').click()
        question_5 = driver.find_element_by_xpath('/html/body/div/form/ul[5]/li[2]/input').click()
        time.sleep(2)
        submit = driver.find_element_by_xpath('/html/body/div/form/input[2]').click()
        time.sleep(2)
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