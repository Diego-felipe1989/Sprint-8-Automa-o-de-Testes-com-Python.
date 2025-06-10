import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # Configurações do Chrome com options e driver manager
        options = Options()
        # Configurar o nível de logging para captura de desempenho
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        # Instala e inicializa o driver do Chrome
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # Configura o tempo de espera implícito
        cls.driver.implicitly_wait(5)

    def test_set_route(self):
        # Abre a URL de rotas urbanas
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        # Configura origem e destino
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        # Verifica se os endereços foram configurados corretamente
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_supportive_plan()
        # Verifica se o plano selecionado é 'Comfort'
        assert routes_page.get_current_selected_plan() == 'Comfort'

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone(data.PHONE_NUMBER)
        # Verifica se o telefone foi preenchido corretamente
        assert routes_page.get_phone() == data.PHONE_NUMBER

    def test_fill_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        # Verifica se o método de pagamento é 'Cartão'
        assert routes_page.get_current_payment_method() == 'Cartão'

    def test_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)
        # Verifica se a mensagem foi configurada
        assert routes_page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_handkerchiefs_option()
        # Verifica se a opção foi marcada
        assert routes_page.get_blanket_and_handkerchiefs_option_checked()

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream(2)
        # Verifica se a quantidade de sorvetes é 2
        assert routes_page.get_amount_of_ice_cream() == 2

    def test_car_search_model_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_taxi_button()
        routes_page.wait_order_taxi_popup()

    def test_driver_info_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_driver_info()
        name, rating, image = routes_page.get_driver_info()
        # Validar se informações do motorista existem
        assert name
        assert rating
        assert image

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
