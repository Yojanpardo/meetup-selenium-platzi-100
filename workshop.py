import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")

    def test_hello_world(self):
        driver = self.driver
        search_term = "documentation"
        driver.get("https://www.python.org")
        about_button = driver.find_element_by_link_text("About")
        sleep(2)
        about_button.click()
        sleep(2)
        search_bar = driver.find_element_by_id("id-search-field")
        search_bar.click()
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.ENTER)
        sleep(2)

    def tearDown(self):
        print("el navegador se va a cerrar....")
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
