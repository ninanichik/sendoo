from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from credentials import credentials


class SkickaPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_vad_skicka(self,  what_sand: str):
        what_sand_field = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div/input")
        what_sand_field.send_keys(what_sand)

    def fill_from_field(self, fields_selector, from_place):
        fran_field = self.driver.find_element_by_css_selector(fields_selector)
        fran_field.send_keys(from_place)
        self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'address-autocomplete-dropdown-container')))
        ActionChains(self.driver).send_keys(u'\ue015').send_keys(u'\ue007').perform()

    def fill_to_field(self, fields_selector, to_place):
        fran_field = self.driver.find_element_by_css_selector(fields_selector)
        fran_field.send_keys(to_place)
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div.address-autocomplete-block:nth-child(2) > div:nth-child(2)')))
        ActionChains(self.driver).send_keys(u'\ue015').send_keys(u'\ue007').perform()

    def click_on_button_transports_type(self, type_of_transport):
        transports_type_btn = self.driver.find_element_by_css_selector(type_of_transport)
        transports_type_btn.click()

    def select_specifik_tid(self):
        select_specific_time = self.driver.find_element_by_css_selector(".css-1aya2g8")
        select_specific_time.click()
        item_specific_time = self.driver.find_element_by_id("react-select-2-option-1")
        item_specific_time.click()

    def input_comment(self, added_comment):
        comment = self.driver.find_element_by_css_selector("div.skicka-textarea-container:nth-child(4) > textarea:nth-child(2)")
        comment.send_keys(added_comment)

    def click_on_loading_type_button(self, kind_of_loading):
        loading_button = self.driver.find_element_by_css_selector(kind_of_loading)
        loading_button.click()

    def click_on_unloading_type_button(self, kind_of_uploading):
        uploading_button = self.driver.find_element_by_css_selector(kind_of_uploading)
        uploading_button.click()


class SkickaProcess(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.skicka = SkickaPage(driver)

    def open(self, driver):
        self.driver.get(credentials.create_skicka_url)

    def loaded(self):
        return self.driver.current_url(credentials.create_skicka_url)

    def fill_skicka_form(
            self, what_sand, from_place, to_place, type_of_transport, added_comment, kind_of_loading, kind_of_uploading):
        self.skicka.fill_vad_skicka(what_sand)
        self.skicka.fill_from_field(
            "div.address-autocomplete-block:nth-child(1) > div:nth-child(1) > input:nth-child(1)",
            from_place)
        self.skicka.fill_to_field(
            "div.address-autocomplete-block:nth-child(2) > div:nth-child(1) > input:nth-child(1)",
            to_place)
        self.skicka.click_on_button_transports_type(type_of_transport)
        self.skicka.input_comment(added_comment)
        self.skicka.click_on_loading_type_button(kind_of_loading)
        self.skicka.click_on_unloading_type_button(kind_of_uploading)

    def click_on_publicera_uppdrag_button(self):
        publish_assignments = self.driver.find_element_by_class_name("btn-success")
        publish_assignments.click()


class CreatedSkicka(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, driver):
        self.wait.until(EC.url_contains(credentials.create_skicka_url))

    def loaded(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-label")))


class CreatedSkickaAuthorizedUser(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, driver):
        self.wait.until(EC.url_contains(credentials.created_skicka_url))

    def loaded(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".img-rotator")))
