from selenium import webdriver
import unittest
from pages.skicka import SkickaProcess, CreatedSkicka, CreatedSkickaAuthorizedUser
from pages.authorization import AuthorizationModal, AuthorizationProcess, SuccessfulAuthorizationPage
from pages.registration import RegistrationProcess, RegistrationIsPassed
from pages.random_email import EmailsGeneration
from credentials import credentials


class MyTestCase(unittest.TestCase):
    def test_authorization(self):
        driver = webdriver.Chrome()
        authorization = AuthorizationProcess(driver)
        authorization.open(driver)
        authorization.fill_authorization_form(credentials.email, credentials.password)
        authorization.click_submit_button()
        assert SuccessfulAuthorizationPage(driver).loaded()

    def test_registration(self):
        driver = webdriver.Chrome()
        registration = RegistrationProcess(driver)
        email = EmailsGeneration().creating_full_email()
        password = EmailsGeneration().creating_random_password()
        registration.open(driver)
        registration.fill_registration_form("name", "surname", email, password, password)
        registration.click_on_submit_button()
        registration.confirm_email_skickat_modal()
        registration.click_on_logga_in()
        assert RegistrationIsPassed(driver).loaded()

    def test_create_skicka(self):
        driver = webdriver.Chrome()
        skicka = SkickaProcess(driver)
        skicka.open(driver)
        skicka.fill_skicka_form("soffa",
                                "Malmö",
                                "Stockholm",
                                "div.transport-block:nth-child(2)",
                                "Lorem ipsum dolor sit amet.",
                                "div.skicka-lists-container:nth-child(1) > div:nth-child(2) > div:nth-child(2)",
                                "div.skicka-lists-container:nth-child(2) > div:nth-child(2) > div:nth-child(3)")
        skicka.click_on_publicera_uppdrag_button()
        assert CreatedSkicka(driver).loaded()


if __name__ == "__main__":
    unittest.main()






