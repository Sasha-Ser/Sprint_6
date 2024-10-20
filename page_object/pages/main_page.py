import allure

from page_object.pages.base_page import BasePage
from page_object.locators.locators_main_page import LocatorsMainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage(BasePage):

    @allure.step('Клик по вопросу')
    def click_to_question(self, question_locator_format):
        self.scroll_to_element(LocatorsMainPage.last_question)
        self.click_to_element(question_locator_format)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        question_locator_format = self.format_locators(LocatorsMainPage.question, num)
        answer_locator_format = self.format_locators(LocatorsMainPage.answer, num)
        self.click_to_question(question_locator_format)
        return self.get_text_from_element(answer_locator_format)

    @allure.step('Переключение на новую вкладку')
    def switching_to_another_tab(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Редирект на главную')
    def redirect_to_main(self, locator, locator_to_main):
        self.click_to_element(locator)
        self.click_to_element(locator_to_main)

    @allure.step('Редирект на яндекс дзен')
    def redirect_to_dzen(self, locator, locator_to_dzen):
        self.click_to_element(locator)
        self.click_to_element(locator_to_dzen)

