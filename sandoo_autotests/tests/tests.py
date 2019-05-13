from selenium import webdriver
import time
import unittest
from pages.skicka import SkickaPage
from pages.authorization import AuthorizationModal
from pages.base_page import BasePage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        authorization = AuthorizationModal(BasePage.web_driver)
        authorization.loaded_modal()
        authorization.fill_email_field("testerwom@gmail.com")
        authorization.fill_password_field("qwertyBasya1")
        authorization.click_submit_button()
        time.sleep(5)
        assert authorization.success_authorization()

    def test_create_skicka(self):
        skicka = SkickaPage(BasePage.web_driver)
        skicka.loaded_skicka()
        skicka.fill_vad_skicka("soffa11")
        skicka.fill_fran_field("Stockholm")
        skicka.fill_till_field("Malmö")
        skicka.click_on_button_transports_type("div.transport-block:nth-child(2)")
        skicka.select_specifik_tid()
        skicka.input_comment("Lorem ipsum dolor sit amet, consectetur adipiscing elit")
        skicka.click_on_loading_type_button("div.skicka-lists-container:nth-child(1) > div:nth-child(2) > div:nth-child(2)")
        skicka.click_on_unloading_type_button("div.skicka-lists-container:nth-child(2) > div:nth-child(2) > div:nth-child(3)")
        skicka.click_on_publicera_uppdrag_button()
        assert skicka.finished_skicka_process()



if __name__ == "__main__":
    unittest.main()






