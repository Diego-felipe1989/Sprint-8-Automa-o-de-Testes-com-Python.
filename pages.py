from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import retrieve_phone_code

import time


class UrbanRoutesPage:
    # Mapeia o campo de endereço de origem pelo atributo ID
    from_field = (By.ID, 'from')  # Busca o elemento com ID "from"

    # Mapeia o campo de endereço de destino pelo atributo ID
    to_field = (By.ID, 'to')  # Busca o elemento com ID "to"

    # Mapeia o botão "Chamar um táxi" usando XPATH
    # O XPATH busca um elemento <button> que contém o texto "Chamar um táxi"
    call_taxi_button = (By.XPATH, '//button[contains(text(), "Chamar um táxi")]')

    # Mapeia os cartões de tarifas pelo atributo CLASS_NAME
    tariff_cards = (By.CLASS_NAME, 'tariff-cards')  # Busca elementos com a classe "tariff-cards"

    # Mapeia o plano "Comfort" usando XPATH
    # O XPATH busca um <div> que contém a classe "tcard" e, dentro dele, outro <div> com o texto "Comfort"
    supportive_plan_card = (By.XPATH, '//div[contains(@class, "tcard")]//div[contains(text(), "Comfort")]')

    # Mapeia o plano ativo usando XPATH
    # O XPATH busca um <div> com a classe "tcard active" e, dentro dele, outro <div> com a classe "tcard-title"
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')

    # Mapeia o controle de número de telefone usando XPATH
    # O XPATH busca um <div> com a classe "np-button" ou que contenha "np-button" e que tenha um <div> com o texto "Número de telefone"
    phone_number_control = (By.XPATH,
                            '//div[@class="np-button" or contains(@class, "np-button")][.//div[contains(text(), "Número de telefone")]]')

    # Mapeia o campo de entrada de número de telefone pelo atributo ID
    phone_number_input = (By.ID, 'phone')  # Busca o elemento com ID "phone"

    # Mapeia o campo de entrada do código de verificação pelo atributo ID
    phone_number_code_input = (By.ID, 'code')  # Busca o elemento com ID "code"

    # Mapeia o botão "Avançar" no formulário de telefone pelo seletor CSS
    # O seletor CSS busca um elemento com a classe "full"
    phone_number_next_button = (By.CSS_SELECTOR, '.full')

    # Mapeia o botão "Confirmar" usando XPATH
    # O XPATH busca um <button> que contém o texto "Confirm"
    phone_number_confirm_button = (By.XPATH, '//button[contains(text(), "Confirm")]')

    # Mapeia o texto exibindo o número de telefone pelo atributo CLASS_NAME
    phone_number = (By.CLASS_NAME, 'np-text')  # Busca o elemento com a classe "np-text"

    # Mapeia o seletor de método de pagamento usando XPATH
    # O XPATH busca um <div> com a classe "pp-button" e que contenha o texto "Método de pagamento"
    payment_method_select = (By.XPATH,
                             '//div[contains(@class, "pp-button")]//div[contains(text(), "Método de pagamento")]')

    # Mapeia o controle para adicionar cartão usando XPATH
    # O XPATH busca um <div> com a classe "pp-title" e que contenha o texto "Adicionar cartão"
    add_card_control = (By.XPATH, '//div[contains(@class, "pp-title") and contains(text(), "Adicionar cartão")]')

    # Mapeia o campo de entrada do número do cartão pelo atributo ID
    card_number_input = (By.ID, 'number')  # Busca o elemento com ID "number"

    # Mapeia o campo de entrada do código do cartão pelo atributo ID
    card_code_input = (By.ID, 'code')  # Busca o elemento com ID "code"

    # Mapeia a imagem de placeholder do cartão pelo atributo CLASS_NAME
    card_plc_image = (By.CLASS_NAME, 'plc')  # Busca o elemento com a classe "plc"

    # Mapeia o botão "Adicionar" para confirmar os dados do cartão usando XPATH
    # O XPATH busca um <button> que contém o texto "Adicionar"
    card_credentials_confirm_button = (By.XPATH, '//button[contains(text(), "Adicionar")]')

    # Mapeia o botão para fechar o seletor de pagamento usando XPATH
    # O XPATH busca um <button> com a classe "close-button section-close" dentro de um <div> com a classe "payment-picker open"
    close_button_payment_method = (By.XPATH,
                                   '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')

    # Mapeia o texto exibindo o método de pagamento atual pelo atributo CLASS_NAME
    current_payment_method = (By.CLASS_NAME, 'pp-value-text')  # Busca o elemento com a classe "pp-value-text"

    # Mapeia o campo de mensagem para o motorista pelo atributo ID
    message_for_driver = (By.ID, 'comment')  # Busca o elemento com ID "comment"

    # Mapeia os interruptores de opções pelo atributo CLASS_NAME
    option_switches = (By.CLASS_NAME, 'switch')  # Busca elementos com a classe "switch"

    # Mapeia os inputs dos interruptores pelo atributo CLASS_NAME
    option_switches_inputs = (By.CLASS_NAME, 'switch-input')  # Busca elementos com a classe "switch-input"

    # Mapeia o botão para adicionar itens enumeráveis pelo atributo CLASS_NAME
    add_enumerable_option = (By.CLASS_NAME, 'counter-plus')  # Busca o elemento com a classe "counter-plus"

    # Mapeia a quantidade de itens enumeráveis pelo atributo CLASS_NAME
    amount_of_enumerable_option = (By.CLASS_NAME, 'counter-value')  # Busca o elemento com a classe "counter-value"

    # Mapeia o botão para pedir um carro pelo atributo CLASS_NAME
    order_car_button = (By.CLASS_NAME, 'smart-button-wrapper')  # Busca o elemento com a classe "smart-button-wrapper"

    # Mapeia o popup de pedido pelo atributo CLASS_NAME
    order_popup = (By.CLASS_NAME, 'order-body')  # Busca o elemento com a classe "order-body"

    # Mapeia a barra de progresso do pedido pelo atributo CLASS_NAME
    progress_bar = (By.CLASS_NAME, 'order-progress visible')  # Busca o elemento com a classe "order-progress visible"

    # Mapeia o tempo de espera do motorista pelo atributo CLASS_NAME
    driver_wait_time = (By.CLASS_NAME, 'order-header-time')  # Busca o elemento com a classe "order-header-time"

    # Mapeia a avaliação do motorista pelo atributo CLASS_NAME
    order_driver_rating = (By.CLASS_NAME, 'order-btn-rating')  # Busca o elemento com a classe "order-btn-rating"

    # Mapeia a imagem do motorista usando XPATH
    # O XPATH busca um <img> dentro de um <div> com a classe "order-button"
    order_driver_image = (By.XPATH, '//div[@class="order-button"]//img')

    # Mapeia o nome do motorista usando XPATH
    # O XPATH busca o segundo <div> dentro do primeiro grupo de botões com a classe "order-btn-group"
    order_driver_name = (By.XPATH, '//div[@class="order-btn-group"][1]/div[2]')

    def __init__(self, driver):
        # Inicializa a página com o driver do Selenium
        self.driver = driver

    def _wait_for(self, locator, timeout=5):
        # Aguarda até que o elemento especificado pelo locator esteja presente no DOM.
        # Utiliza o WebDriverWait para esperar até que a condição de presença seja atendida.
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )

    def _wait_for_visible(self, locator, timeout=5):
        # Aguarda até que o elemento especificado pelo locator esteja visível na página.
        # Utiliza o WebDriverWait para esperar até que a condição de visibilidade seja atendida.
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def set_from(self, from_address):
        # Preenche o campo de endereço de origem com o valor fornecido.
        # Aguarda até que o campo esteja visível antes de enviar o texto.
        self._wait_for_visible(self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        # Preenche o campo de endereço de destino com o valor fornecido.
        # Aguarda até que o campo esteja visível antes de enviar o texto.
        self._wait_for_visible(self.to_field).send_keys(to_address)

    def get_from(self):
        # Retorna o valor atual do campo de endereço de origem.
        # Aguarda até que o campo esteja presente no DOM antes de obter o valor.
        return self._wait_for(self.from_field).get_property('value')

    def get_to(self):
        # Retorna o valor atual do campo de endereço de destino.
        # Aguarda até que o campo esteja presente no DOM antes de obter o valor.
        return self._wait_for(self.to_field).get_property('value')

    def click_call_taxi_button(self):
        # Clica no botão "Chamar um táxi".
        # Aguarda até que o botão esteja visível antes de realizar a ação de clique.
        self._wait_for_visible(self.call_taxi_button).click()

    def set_route(self, from_address, to_address):
        # Configura a rota preenchendo os endereços de origem e destino e clicando no botão de chamada.
        # Primeiro, preenche o campo de origem.
        self.set_from(from_address)
        # Em seguida, preenche o campo de destino.
        self.set_to(to_address)
        # Por fim, clica no botão para chamar o táxi.
        self.click_call_taxi_button()

    def select_supportive_plan(self):
        # Seleciona o plano de suporte "Comfort".
        # Aguarda até que o cartão do plano esteja visível.
        card = self._wait_for_visible(self.supportive_plan_card)
        # Rola a página até o elemento para garantir que ele esteja visível na viewport.
        self.driver.execute_script("arguments[0].scrollIntoView();", card)
        # Clica no cartão para selecionar o plano.
        card.click()

    def get_current_selected_plan(self):
        # Retorna o nome do plano atualmente selecionado.
        # Aguarda até que o elemento do plano ativo esteja presente no DOM antes de obter o texto.
        return self._wait_for(self.active_plan_card).text

    def set_phone(self, number):
        # Preenche o número de telefone no formulário e confirma o código de verificação.
        # Primeiro, clica no controle de número de telefone.
        self._wait_for(self.phone_number_control).click()
        # Em seguida, preenche o campo de entrada com o número fornecido.
        self._wait_for(self.phone_number_input).send_keys(number)
        # Clica no botão "Avançar".
        self._wait_for(self.phone_number_next_button).click()
        # Obtém o código de verificação (simulado pelo helper).
        code = retrieve_phone_code(self.driver)
        # Preenche o campo de código de verificação com o código obtido.
        self._wait_for(self.phone_number_code_input).send_keys(code)
        # Clica no botão "Confirmar" para finalizar o processo.
        self._wait_for(self.phone_number_confirm_button).click()

    def get_phone(self):
        # Retorna o número de telefone configurado.
        # Aguarda até que o elemento exibindo o número esteja presente no DOM antes de obter o texto.
        return self._wait_for(self.phone_number).text

    def set_card(self, card_number, code):
        # Preenche os dados do cartão de crédito e confirma.
        # Primeiro, clica no seletor de método de pagamento.
        self.driver.find_element(*self.payment_method_select).click()
        # Aguarda brevemente para garantir que o seletor esteja carregado.
        self.driver.implicitly_wait(2)
        # Clica no controle para adicionar um novo cartão.
        self.driver.find_element(*self.add_card_control).click()
        # Preenche o número do cartão e o código de segurança.
        self.driver.find_element(*self.card_number_input).send_keys(card_number + Keys.TAB + code)
        # Clica na imagem de placeholder para confirmar os dados.
        self.driver.find_element(*self.card_plc_image).click()
        # Clica no botão "Adicionar" para salvar o cartão.
        self.driver.find_element(*self.card_credentials_confirm_button).click()
        # Fecha o seletor de método de pagamento.
        self.driver.find_element(*self.close_button_payment_method).click()

    def get_current_payment_method(self):
        # Retorna o método de pagamento atualmente selecionado.
        # Aguarda até que o elemento exibindo o método esteja presente no DOM antes de obter o texto.
        return self._wait_for(self.current_payment_method).text

    def set_message_for_driver(self, message):
        # Preenche o campo de mensagem para o motorista com o texto fornecido.
        # Aguarda até que o campo esteja visível antes de enviar o texto.
        self._wait_for(self.message_for_driver).send_keys(message)

    def get_message_for_driver(self):
        # Retorna a mensagem configurada para o motorista.
        # Aguarda até que o campo esteja presente no DOM antes de obter o valor.
        return self._wait_for(self.message_for_driver).get_property('value')

    def click_blanket_and_handkerchiefs_option(self):
        # Seleciona a opção de cobertor e lenços.
        # Aguarda até que os interruptores estejam presentes no DOM.
        switches = WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_all_elements_located(self.option_switches)
        )
        # Clica no primeiro interruptor para ativar a opção.
        switches[0].click()
        # Verifica se a opção foi marcada corretamente.
        self.get_blanket_and_handkerchiefs_option_checked()

    def get_blanket_and_handkerchiefs_option_checked(self):
        # Verifica se a opção de cobertor e lenços está marcada.
        # Aguarda até que os inputs dos interruptores estejam presentes no DOM.
        switches = WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_all_elements_located(self.option_switches_inputs)
        )
        # Retorna o estado do primeiro interruptor (marcado ou não).
        return switches[0].get_property('checked')

    def add_ice_cream(self, amount: int):
        # Adiciona a quantidade especificada de sorvetes ao pedido.
        # Aguarda até que os controles de adição estejam presentes no DOM.
        option_add_controls = WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_all_elements_located(self.add_enumerable_option)
        )
        # Rola a página até o primeiro controle para garantir visibilidade.
        self.driver.execute_script("arguments[0].scrollIntoView();", option_add_controls[0])
        # Clica no botão de adição a quantidade de vezes especificada.
        for _ in range(amount):
            option_add_controls[0].click()

    def get_amount_of_ice_cream(self):
        # Retorna a quantidade de sorvetes adicionada ao pedido.
        # Aguarda até que o elemento exibindo a quantidade esteja presente no DOM.
        return int(WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_all_elements_located(self.amount_of_enumerable_option)
        )[0].text)

    def click_order_taxi_buton(self):
        # Clica no botão para pedir um táxi.
        # Aguarda até que o botão esteja presente no DOM antes de realizar a ação de clique.
        self._wait_for(self.order_car_button).click()

    def wait_order_taxi_popup(self):
        # Aguarda até que o popup de pedido de táxi apareça.
        # Utiliza o método _wait_for_visible para garantir que o popup esteja visível.
        self._wait_for_visible(self.order_popup)

    def wait_driver_info(self):
        # Aguarda até que as informações do motorista estejam disponíveis.
        # Primeiro, espera que o tempo de espera do motorista desapareça.
        WebDriverWait(self.driver, 60).until(
            expected_conditions.invisibility_of_element_located(self.driver_wait_time)
        )
        # Aguarda até que os elementos de avaliação, imagem e nome do motorista estejam presentes no DOM.
        self._wait_for(self.order_driver_rating)
        self._wait_for(self.order_driver_image)
        self._wait_for(self.order_driver_name)

    def get_driver_info(self):
        # Retorna as informações do motorista (nome, avaliação e imagem).
        # Obtém o texto da avaliação do motorista.
        rating = self._wait_for(self.order_driver_rating).text
        # Obtém o link da imagem do motorista.
        image = self._wait_for(self.order_driver_image).get_property('src')
        # Obtém o nome do motorista.
        name = self._wait_for(self.order_driver_name).text
        # Retorna os dados como uma tupla.
        return name, rating, image
