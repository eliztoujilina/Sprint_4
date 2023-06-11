def test_order_buttons():
    # Открываем главную страницу
    driver.get("https://qa-scooter.praktikum-services.ru/")

    # Подтверждаем использование куки
    cookie_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_CONFIRM_BUTTON))
    cookie_button.click()

    # Проверяем кнопку "Заказать" в шапке сайта
    header_order_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.HEADER_ORDER_BUTTON))
    header_order_button.click()

    # Проверяем переход в форму "Для кого" самоката
    registration_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.TITLE_REGISTER_FORM))
    assert registration_title.is_displayed()

    driver.back()

    # Проверяем кнопку "Заказать" в середине сайта
    middle_order_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.MIDDLE_ORDER_BUTTON))
    middle_order_button.click()

    # Проверяем переход в форму "Для кого" самоката
    registration_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.TITLE_REGISTER_FORM))
    assert registration_title.is_displayed()

    print("Test for order buttons passed successfully.")


test_order_buttons()
