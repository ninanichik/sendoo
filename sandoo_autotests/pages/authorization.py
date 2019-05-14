from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AuthorizationModal(BasePage):
    def loaded_modal(self):
        self.driver.get("")
        login_button = self.driver.find_element_by_link_text("LOGGA IN")
        login_button.click()

    def fill_email_field(self, email):
        email_field = self.driver.find_element_by_css_selector(".login-form > form:nth-child(4) > input:nth-child(1)")
        email_field.send_keys(email)

    def fill_password_field(self, password):
        email_field = self.driver.find_element_by_css_selector(".login-form > form:nth-child(4) > input:nth-child(2)")
        email_field.send_keys(password)

    def click_submit_button(self):
        submit_button = self.driver.find_element_by_css_selector("#modal-root > div > div > form > input[type='submit']:nth-child(3)")
        submit_button.click()

    def success_authorization(self):
        return self.driver.find_element_by_css_selector(".message")




