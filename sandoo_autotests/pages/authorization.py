from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from credentials import credentials


class AuthorizationModal:
    def __init__(self, driver):
        self.driver = driver

    def fill_email_field(self, email):
        email_field = self.driver.find_element_by_css_selector(".login-form > form:nth-child(4) > input:nth-child(1)")
        email_field.send_keys(email)

    def fill_password_field(self, password):
        email_field = self.driver.find_element_by_css_selector(".login-form > form:nth-child(4) > input:nth-child(2)")
        email_field.send_keys(password)


class AuthorizationProcess(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.authorization = AuthorizationModal(driver)

    def open(self, driver):
        self.driver.get(credentials.base_url)
        login_button = self.driver.find_element_by_link_text("LOGGA IN")
        login_button.click()

    def loaded(self):
        return "Sendoo" in self.driver.title

    def fill_authorization_form(self, email, password):
        self.authorization.fill_email_field(email)
        self.authorization.fill_password_field(password)

    def click_submit_button(self):
        submit_button = self.driver.find_element_by_css_selector("#modal-root > div > div > form > input[type='submit']:nth-child(3)")
        submit_button.click()


class SuccessfulAuthorizationPage(BasePage):
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def open(self, driver):
        self.driver.get(credentials.create_skicka_url)

    def loaded(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".message")))



