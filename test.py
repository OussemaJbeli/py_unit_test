from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class w3schooldsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Selenium will find ChromeDriver in PATH

# test connection
    def test_website_title(self):
        driver = self.driver
        driver.get("https://boontest.netlify.app/")
        self.assertIn("BOON ", driver.title)
        time.sleep(5)
# test open sidebar
    def test_opensidebar(self):
        driver = self.driver
        driver.get("https://boontest.netlify.app/")
        search = driver.find_element(By.ID, 'openSideBar')
        search.send_keys(Keys.RETURN)
        self.assertIn("open sidebar")
        time.sleep(2)
# test change language
    def test_changeLanguage(self):
        driver = self.driver
        driver.get("https://boontest.netlify.app/")
        search = driver.find_element(By.ID, 'languageButton')
        search.send_keys(Keys.RETURN)
        self.assertIn("open sidebar")
        time.sleep(2)

    def test_selectArabic(self):
        driver = self.driver
        driver.get("https://boontest.netlify.app/")
        search = driver.find_element(By.ID, 'arabicSwitsh')
        search.send_keys(Keys.RETURN)
        self.assertIn("open sidebar")
        time.sleep(2)
# test change mode
    def test_changeMode(self):
        driver = self.driver
        driver.get("https://boontest.netlify.app/")
        search = driver.find_element(By.ID, 'modeButton')
        search.send_keys(Keys.RETURN)
        self.assertIn("open sidebar")
        time.sleep(2)

    def test_selectDark(self):
        driver = self.driver
        driver.get("https://boontest.netlify.app/")
        search = driver.find_element(By.ID, 'darkModeSwitsh')
        search.send_keys(Keys.RETURN)
        self.assertIn("open sidebar")
        time.sleep(2)
# test close didebar
    def test_closesidebar(self):
        driver = self.driver
        driver.get("https://boontest.netlify.app/")
        search = driver.find_element(By.ID, 'closeSideBar')
        search.send_keys(Keys.RETURN)
        self.assertIn("open sidebar")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()