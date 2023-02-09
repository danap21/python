import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import page

class Swag_Lab_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.saucedemo.com")
   
    #Test Swag Labs login page
    def test_swag_login_page(self):
        
        #Load Main Page
        main_page = page.MainPage(self.driver)

        #Checks if the Title is Swag Labs
        self.assertTrue(main_page.is_title_matches(), " Title is not Swag Labs")
    
    def test_login_button(self):
        main_page = page.MainPage(self.driver)
        main_page.click_login_button()
        self.driver.implicitly_wait(5)
        pass
    
    def test_no_input_credentials(self):
        #Test that we get an error when no credentials are provided for input
        main_page = page.MainPage(self.driver)
        main_page.click_login_button()

        def check_login_error(self):
            if self.driver.find_element(By.XPATH, '//*[@class="error-button" and contains(@title="Epic sadface: Username is required")]'):
                True
            else:
                False
        self.assertTrue(check_login_error(self), "No error found")
   
    def test_login_success(self): 
        #Test login success with correct credentials and redirect to Inventory page
        main_page = page.MainPage(self.driver)
        main_page.login_credentials_pass()

        redirect_url = self.driver.current_url
        print("Redirected to " + redirect_url)
        login_url = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(redirect_url, login_url)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

    