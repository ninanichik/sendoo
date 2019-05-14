from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from credentials import credentials


class RegistrationModal:
    def __init__(self, driver):
        self.driver = driver

    def fill_name_field(self, user_name):
        name_field = self.driver.find_element_by_css_selector(".login-form > form:nth-child(4) > input:nth-child(1)")
        name_field.send_keys(user_name)

    def fill_surname_field(self, user_surname):
        surname_field = self.driver.find_element_by_css_selector(".login-form > form:nth-child(4) > input:nth-child(2)")
        surname_field.send_keys(user_surname)

    def fill_email(self, email):
        email_field = self.driver.find_element_by_css_selector(".login-form > form:nth-child(4) > input:nth-child(3)")
        email_field.send_keys(email)

    def fill_password(self, password):
        password_field = self.driver.find_element_by_css_selector(".login-form > form:nth-child(4) > input:nth-child(4)")
        password_field.send_keys(password)

    def fill_confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element_by_css_selector(".login-form > form:nth-child(4) > input:nth-child(5)")
        confirm_password_field.send_keys(confirm_password)


class RegistrationProcess(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.registration = RegistrationModal(driver)

    def open(self, driver):
        self.driver.get(credentials.base_url)
        login_button = self.driver.find_element_by_link_text("LOGGA IN")
        login_button.click()
        logup_button = self.driver.find_element_by_link_text("Skapa konto")
        logup_button.click()

    def loaded(self):
        return "Sendoo" in self.driver.title

    def fill_registration_form(self, user_name, user_surname, email, password, confirm_password):
        self.registration.fill_name_field(user_name)
        self.registration.fill_surname_field(user_surname)
        self.registration.fill_email(email)
        self.registration.fill_password(password)
        self.registration.fill_confirm_password(confirm_password)

    def click_on_submit_button(self):
        submit_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-form > form:nth-child(4) > input:nth-child(6)")))
        submit_button.click()

    def confirm_email_skickat_modal(self):
        confirm_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/input")))
        confirm_button.click()

    def click_on_logga_in(self):
        logga_in = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/form/input[3]")))
        logga_in.click()


class RegistrationIsPassed(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, driver):
        self.driver.get(credentials.create_skicka_url)

    def loaded(self):
        return self.wait.until(EC.url_matches("http://18.195.233.16:35622/overview/new"))

