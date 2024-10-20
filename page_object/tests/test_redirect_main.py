import pytest
import allure

from page_object.pages.main_page import MainPage, BasePage
from page_object.locators.locators_main_page import LocatorsMainPage


class TestRedirectToMain:

    @allure.title('Проверка на редирект на главную страницу')
    def test_redirect_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.redirect_to_main(LocatorsMainPage.button_order_header, LocatorsMainPage.button_to_main)
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'