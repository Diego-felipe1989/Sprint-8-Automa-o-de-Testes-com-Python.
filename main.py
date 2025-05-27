import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Verifica se o servidor está ativo
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        # Adicionar em S8
        print("Criando função test_set_route")
        pass

    def test_select_plan(self):
        # Adicionar em S8
        print("Criando função test_select_plan")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("Criando função test_fill_phone_number")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("Criando função test_fill_card")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("Criando função test_comment_for_driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("Criando função test_order_blanket_and_handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        print("Criando função test_order_2icecreams")
        for count in range(2):
            # Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("Criando função test_car_search_model_appears")
        pass