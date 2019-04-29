from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SkickaPage(BasePage):
    def loaded_skicka(self):
        self.driver.get("http://18.195.233.16:35622/package/create")

    def fill_vad_skicka(self,  what_sand: str):
        what_sand_field = self.driver.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div/input")
        what_sand_field.send_keys(what_sand)

    def fill_fran_field(self, from_place):
        fran_field = self.driver.find_element_by_css_selector("div.address-autocomplete-block:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        fran_field.send_keys(from_place)
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'address-autocomplete-dropdown-container')))
        ActionChains(self.driver).send_keys(u'\ue015').send_keys(u'\ue007').perform()

    def fill_till_field(self, to_place):
        till_field = self.driver.find_element_by_css_selector("div.address-autocomplete-block:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        till_field.send_keys(to_place)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.address-autocomplete-block:nth-child(2) > div:nth-child(2)')))
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

    def click_on_publicera_uppdrag_button(self):
        publish_assignments = self.driver.find_element_by_class_name("btn-success")
        publish_assignments.click()

    def finished_skicka_process(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".img-rotator")))

