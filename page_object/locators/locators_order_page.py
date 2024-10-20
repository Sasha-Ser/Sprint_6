from selenium.webdriver.common.by import By


class LocatorsOrderPage:

    button_cookie = By.XPATH, "//button[@class='App_CookieButton__3cvqF']" #Локатор кнопки подтверждения куки
    name_input = By.XPATH, "//input[@placeholder = '* Имя']" #Локатор поля "Имя"
    femail_input = By.XPATH, "//input[@placeholder = '* Фамилия']" #Локатор поля "Фамилия"
    adress_input = By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']" #Локатор поля "Адрес"
    metro_station_input = By.XPATH, "//input[@placeholder = '* Станция метро']" #Локатор поля "Станция метро"
    choice_metro_station = By.XPATH, "//button[@value = '1']" #Локатор первой станции из выпадающего списка
    phone_number_input = By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']" #Локатор поля "Телефон"
    button_next_first_screen = By.XPATH, "//button[text()='Далее']" #Локатор кнопки "Далее"
    date_input = By.XPATH, "//input[@placeholder = '* Когда привезти самокат']" #Локатор поля "Когда привезти самокат"
    rental_period = By.XPATH, "//div[text() = '* Срок аренды']" #Локатор поля "Срок аренды"
    day_select = By.XPATH, "//div[text() = 'двое суток']" #Локатор варианта из выпадающего списка для срока аренды
    color_samokat = By.XPATH, "//*[@id='black']" #Локатор чекбокса черного цвета самоката "Имя"
    button_order_header = By.XPATH, "//button[@class = 'Button_Button__ra12g']" #Локатор кнопки "Заказать" в хедере
    button_order_bottom= By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']" #Локатор кнопки "Заказать" в середине экрана
    agree_order = By.XPATH, "//button[text()= 'Да']" #Локатор кнопки "Да" экрана "Хотите оформить заказ"
    status_information = By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ']" #Локатор текста с подтверждением заказа
