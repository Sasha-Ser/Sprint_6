from page_object.pages.base_page import BasePage
from page_object.locators.locators_order_page import LocatorsOrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from page_object.data import Data
import allure

class OrderPage(BasePage):

    @allure.step('Заполнение данных на первом экране создания заказа')
    def order_first_screen(self, button_order_page):
        self.click_to_element(LocatorsOrderPage.button_cookie)
        self.click_to_element(button_order_page)
        self.add_text_to_element(LocatorsOrderPage.name_input , Data.name_order)
        self.add_text_to_element(LocatorsOrderPage.femail_input, Data.femail_order)
        self.add_text_to_element(LocatorsOrderPage.adress_input, Data.adress_order)
        self.click_to_element(LocatorsOrderPage.metro_station_input)
        self.click_to_element(LocatorsOrderPage.choice_metro_station)
        self.add_text_to_element(LocatorsOrderPage.phone_number_input, Data.phone_order)
        self.click_to_element(LocatorsOrderPage.button_next_first_screen)

    @allure.step('Заполнение данных на втором экране создания заказа и подтверждение заказа')
    def order_second_screen(self):
        self.add_text_to_element(LocatorsOrderPage.date_input, Data.date_order)
        self.find_element_with_wait(LocatorsOrderPage.date_input).send_keys(Keys.ENTER)
        self.click_to_element(LocatorsOrderPage.rental_period)
        self.find_element_with_wait(LocatorsOrderPage.day_select)
        self.click_to_element(LocatorsOrderPage.day_select)
        self.click_to_element(LocatorsOrderPage.color_samokat)
        self.click_to_element(LocatorsOrderPage.button_order_bottom)
        self.click_to_element(LocatorsOrderPage.agree_order)
