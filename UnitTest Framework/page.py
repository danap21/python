from element import BasePageElement
from locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        #Verify "Swag Labs" is in the title
        return "Swag Labs" in self.driver.title
       

    def click_login_button(self):
        login_button = self.driver.find_element(*MainPageLocators.Login_Button)
        login_button.click()    
    
    def login_credentials_pass(self):
        enter_username = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        enter_username.send_keys("standard_user")
        
        enter_password = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        enter_password.send_keys("secret_sauce" + Keys.ENTER)
        redirect_url = self.driver.current_url
        print("Redirected to " + redirect_url)
        login_url = "https://www.saucedemo.com/inventory.html"
        if redirect_url == login_url:
                return True
        else: 
                return False

