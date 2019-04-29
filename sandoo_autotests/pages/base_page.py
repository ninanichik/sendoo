from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    web_driver = webdriver.Chrome()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # self.driver.implicitly_wait(10)
