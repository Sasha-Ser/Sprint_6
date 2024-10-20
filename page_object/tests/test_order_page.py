import pytest
import allure

from page_object.pages.order_page import OrderPage
from page_object.locators.locators_order_page import LocatorsOrderPage


class TestOrder:

    @allure.title('Проверка создания заказа через кнопку "Заказать" в хедере')
    def test_order_header_button(self, driver):
        order_page = OrderPage(driver)
        order_page.order_first_screen(LocatorsOrderPage.button_order_header)
        order_page.order_second_screen()
        title = order_page.get_text_from_element(LocatorsOrderPage.status_information)
        assert 'Заказ оформлен' in title

    @allure.title('Проверка создания заказа через кнопку "Заказать" в середине экрана')
    def test_order_bottom_button(self, driver):
        order_page = OrderPage(driver)
        order_page.order_first_screen(LocatorsOrderPage.button_order_bottom)
        order_page.order_second_screen()
        title = order_page.get_text_from_element(LocatorsOrderPage.status_information)
        assert 'Заказ оформлен' in title