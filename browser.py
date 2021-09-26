import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Browser:
    def __init__(self, username):
        self.username = username
        driver_Path = "chromedriver.exe"
        self.browser = webdriver.Chrome(driver_Path)
        Browser.goSearchPage(self)

    def goSearchPage(self):
        self.browser.get("https://app.htcert.com/view/search/")
        Browser.searchdata(self)
        Browser.whileloop(self)
    def searchdata(self):
        username_field = self.browser.find_element_by_name("filter_133")
        username_field.send_keys(self.username)
        username_field.send_keys(Keys.ENTER)
        time.sleep(3)
        
        
    def whileloop(self):
        username_field = self.browser.find_element_by_name("filter_133").clear()
        time.sleep(4)


        i = 1000

        while i<=1999:
            i += 1

            deneme_field = self.browser.find_element_by_name("filter_133")
            deneme_field.send_keys( str(i) +  'C04201001')
            deneme_field.send_keys(Keys.ENTER)
            time.sleep(5)
            username_field = self.browser.find_element_by_name("filter_133").clear()
            print('Loop ended.')
