from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest
import time

class BoonTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://boontest.netlify.app/")
        self.wait = WebDriverWait(self.driver, 10)
        time.sleep(2)  

    def wait_and_click(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        element.click()

    def test_website_title(self):
        self.assertIn("Boon", self.driver.title)

    def test_open_sidebar(self):
        self.wait_and_click(By.ID, 'openSideBar')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'closeSideBar')))

    def test_change_language(self):
        self.wait_and_click(By.ID, 'openSideBar')
        self.wait_and_click(By.ID, 'languageButton')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'arabicSwitsh')))

    def test_select_arabic(self):
        self.wait_and_click(By.ID, 'openSideBar')
        self.wait_and_click(By.ID, 'languageButton')
        self.wait_and_click(By.ID, 'arabicSwitsh')
        self.wait.until(lambda d: "نص عربي" in d.page_source)

    def test_change_mode(self):
        self.wait_and_click(By.ID, 'openSideBar')
        self.wait_and_click(By.ID, 'modeButton')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'darkModeSwitsh')))

    def test_select_dark_mode(self):
        self.wait_and_click(By.ID, 'openSideBar')
        self.wait_and_click(By.ID, 'modeButton')
        self.wait_and_click(By.ID, 'darkModeSwitsh')
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dark")))

    def test_close_sidebar(self):
        self.wait_and_click(By.ID, 'openSideBar')
        time.sleep(1)
        self.wait_and_click(By.ID, 'closeSideBar')
        self.wait.until(EC.invisibility_of_element_located((By.ID, 'closeSideBar')))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
