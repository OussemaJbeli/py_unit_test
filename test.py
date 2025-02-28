from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class w3schooldsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Selenium will find ChromeDriver in PATH

    def test_website_title(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/")
        print('first print with TITLE : ',driver.title)
        self.assertIn("W3Schools", driver.title)

    def test_search_bar(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/")
        search = driver.find_element(By.ID, 'tnb-google-search-input')
        search.send_keys("python")
        search.send_keys(Keys.RETURN)
        time.sleep(15)
        self.assertIn("Python", driver.title)
        assert "Python" in driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()