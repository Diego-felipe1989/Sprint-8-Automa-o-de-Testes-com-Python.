from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.address_input = (By.ID, 'address-input')
        self.comfort_radio = (By.ID, 'tarifa-comfort')
        self.phone_input = (By.ID, 'phone')
        self.add_card_button = (By.ID, 'add-card-btn')
        self.card_number_input = (By.ID, 'card-number')
        self.card_expiry_input = (By.ID, 'card-expiry')
        self.card_cvv_input = (By.ID, 'code')
        self.comment_textarea = (By.ID, 'comment')
        self.blankets_button = (By.ID, 'request-blankets')
        self.tissues_button = (By.ID, 'request-tissues')
        self.ice_cream_button = (By.ID, 'request-ice-cream')
        self.tarifa_comfort = (By.ID, 'tarifa-comfort')
        self.request_button = (By.ID, 'request-taxi')
        self.car_search_modal = (By.ID, 'car-search-modal')

    def _wait_for(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def _wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def open_url(self, url):
        self.driver.get(url)

    def set_address(self, address):
        address_field = self._wait_for_visible(self.address_input)
        address_field.clear()
        address_field.send_keys(address)

    def is_comfort_selected(self):
        try:
            comfort_radio = self.driver.find_element(*self.comfort_radio)
            return comfort_radio.is_selected()
        except:
            return False

    def select_comfort(self):
        comfort_radio = self._wait_for_visible(self.comfort_radio)
        comfort_radio.click()

    def retrieve_phone_code(self):
        from helpers import retrieve_phone_code
        return retrieve_phone_code()

    def fill_phone(self, phone):
        phone_field = self._wait_for_visible(self.phone_input)
        phone_field.clear()
        phone_field.send_keys(phone)

    def click_add_card(self):
        button = self._wait_for_visible(self.add_card_button)
        button.click()

    def fill_card_details(self, number, expiry, cvv):
        number_field = self._wait_for_visible(self.card_number_input)
        number_field.clear()
        number_field.send_keys(number)

        expiry_field = self._wait_for_visible(self.card_expiry_input)
        expiry_field.clear()
        expiry_field.send_keys(expiry)

        cvv_field = self._wait_for_visible(self.card_cvv_input)
        cvv_field.clear()
        cvv_field.send_keys(cvv)
        cvv_field.send_keys(Keys.TAB)  # para perder foco e ativar o campo

    def write_comment(self, comment):
        comment_box = self._wait_for_visible(self.comment_textarea)
        comment_box.clear()
        comment_box.send_keys(comment)

    def request_blankets_and_tissues(self):
        blankets_btn = self._wait_for_visible(self.blankets_button)
        blankets_btn.click()
        tissues_btn = self._wait_for_visible(self.tissues_button)
        tissues_btn.click()

    def is_blankets_requested(self):
        try:
            btn = self.driver.find_element(*self.blankets_button)
            return 'requested' in btn.get_attribute('class')
        except:
            return False

    def is_tissues_requested(self):
        try:
            btn = self.driver.find_element(*self.tissues_button)
            return 'requested' in btn.get_attribute('class')
        except:
            return False

    def request_ice_cream(self):
        btn = self._wait_for_visible(self.ice_cream_button)
        btn.click()

    def select_tarifa(self, tarifa_name):
        if tarifa_name.lower() == 'comfort':
            tarifa_element = self._wait_for_visible(self.tarifa_comfort)
            tarifa_element.click()
        # Adicione outros tarifas se necessário

    def confirm_request(self, message):
        request_btn = self._wait_for_visible(self.request_button)
        request_btn.click()
        # opcional: aguardar modal de confirmação
        self._wait_for_visible(self.car_search_modal)

    def is_car_search_modal_visible(self):
        try:
            modal = self.driver.find_element(*self.car_search_modal)
            return modal.is_displayed()
        except:
            return False
