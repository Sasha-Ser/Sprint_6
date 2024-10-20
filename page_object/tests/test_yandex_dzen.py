import pytest
import allure

from page_object.pages.main_page import MainPage
from page_object.locators.locators_main_page import LocatorsMainPage, LocatorDzen


class TestYandexDzen:

    @allure.title('Проверка на редирект на страницу яндекс.дзен')
    def test_redirect_yandex_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.redirect_to_dzen(LocatorsMainPage.button_order_header, LocatorsMainPage.button_to_dzen)
        main_page.switching_to_another_tab(LocatorDzen.locator_dzen)
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

