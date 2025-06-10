import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # Configura o navegador Chrome com opções específicas
        options = Options()
        # Define o nível de logging para capturar informações de desempenho
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        # Inicializa o driver do Chrome com as opções configuradas
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # Define um tempo de espera implícito para encontrar elementos na página
        cls.driver.implicitly_wait(5)

    def test_set_route(self):
        # Abre a URL da página de rotas urbanas
        self.driver.get(data.URBAN_ROUTES_URL)
        # Cria uma instância da página de rotas urbanas
        routes_page = UrbanRoutesPage(self.driver)
        # Define os endereços de origem e destino
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        # Configura a rota com os endereços fornecidos
        routes_page.set_route(address_from, address_to)
        # Verifica se o endereço de origem foi configurado corretamente
        assert routes_page.get_from() == address_from
        # Verifica se o endereço de destino foi configurado corretamente
        assert routes_page.get_to() == address_to

    def test_select_plan(self):
        # Cria uma instância da página de rotas urbanas
        routes_page = UrbanRoutesPage(self.driver)
        # Seleciona o plano de suporte "Comfort"
        routes_page.select_supportive_plan()
        # Verifica se o plano selecionado é "Comfort"
        assert routes_page.get_current_selected_plan() == 'Comfort'

    def test_fill_phone_number(self):
        # Cria uma instância da página de rotas urbanas
        routes_page = UrbanRoutesPage(self.driver)
        # Define o número de telefone a ser preenchido
        phone_number = data.PHONE_NUMBER
        # Preenche o número de telefone no formulário
        routes_page.set_phone(phone_number)
        # Verifica se o número de telefone foi configurado corretamente
        assert routes_page.get_phone() == phone_number

    def test_fill_card(self):
        # Cria uma instância da página de rotas urbanas
        routes_page = UrbanRoutesPage(self.driver)
        # Preenche os dados do cartão de crédito (número e código)
        routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        # Verifica se o método de pagamento atual é "Cartão"
        assert routes_page.get_current_payment_method() == 'Cartão'

    def test_comment_for_driver(self):
        # Cria uma instância da página de rotas urbanas
        routes_page = UrbanRoutesPage(self.driver)
        # Define a mensagem para o motorista
        message = data.MESSAGE_FOR_DRIVER
        # Adiciona a mensagem no campo apropriado
        routes_page.set_message_for_driver(message)
        # Verifica se a mensagem foi configurada corretamente
        assert routes_page.get_message_for_driver() == message

    def test_order_blanket_and_handkerchiefs(self):
        # Cria uma instância da página de rotas urbanas
        routes_page = UrbanRoutesPage(self.driver)
        # Seleciona a opção de cobertor e lenços
        routes_page.click_blanket_and_handkerchiefs_option()
        # Verifica se a opção foi marcada corretamente
        assert routes_page.get_blanket_and_handkerchiefs_option_checked()

    def test_order_2_ice_creams(self):
        # Cria uma instância da página de rotas urbanas
        routes_page = UrbanRoutesPage(self.driver)
        # Adiciona 2 sorvetes ao pedido
        routes_page.add_ice_cream(2)
        # Verifica se a quantidade de sorvetes adicionada é 2
        assert routes_page.get_amount_of_ice_cream() == 2

    def test_car_search_model_appears(self):
        # Cria uma instância da página de rotas urbanas
        routes_page = UrbanRoutesPage(self.driver)
        # Clica no botão para pedir um táxi
        routes_page.click_order_taxi_buton()
        # Aguarda o popup de pedido de táxi aparecer
        routes_page.wait_order_taxi_popup()

    def test_driver_info_appears(self):
        # Cria uma instância da página de rotas urbanas
        routes_page = UrbanRoutesPage(self.driver)
        # Aguarda as informações do motorista aparecerem
        routes_page.wait_driver_info()
        # Obtém as informações do motorista (nome, avaliação e imagem)
        name, rating, image = routes_page.get_driver_info()
        # Verifica se o nome do motorista está presente
        assert name
        # Verifica se a avaliação do motorista está presente
        assert rating
        # Verifica se a imagem do motorista está presente
        assert image

    @classmethod
    def teardown_class(cls):
        # Fecha o navegador após a execução de todos os testes
        cls.driver.quit()
