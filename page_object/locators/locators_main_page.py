from selenium.webdriver.common.by import By


class LocatorsMainPage:

    question = By.ID, 'accordion__heading-{}' #Локатор для вопроса
    answer = By.ID, 'accordion__panel-{}' #Локатор для ответа
    last_question = By.ID, 'accordion__heading-7' #Локатор последнего ответа
    button_to_dzen = By.CLASS_NAME, 'Header_LogoYandex__3TSOI' #Локатор для вопроса
    button_order_header = By.XPATH, ".//button[@class = 'Button_Button__ra12g']" #Локатор кнопки "Заказать" в Хедере
    button_order_bottom = By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']" #Локатор кнопки "Заказать" в блоке "Как это работает"
    button_to_main = By.CLASS_NAME, 'Header_LogoScooter__3lsAR' #Локатор кнопки "Самокат"

class LocatorDzen:

    locator_dzen = By.XPATH, ".//button[text()='Найти']" #Локатор кнопки "Яндекс"