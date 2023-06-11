def test_yandex_logo_redirect():
    # Открываем главную страницу
    driver.get("https://qa-scooter.praktikum-services.ru/")

    # Подтверждаем использование куки
    cookie_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_CONFIRM_BUTTON))
    cookie_button.click()

    # Нажимаем на логотип "Яндекс"
    yandex_logo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGO_YANDEX))
    yandex_logo.click()

    # Переключаемся на новое окно
    driver.switch_to.window(driver.window_handles[1])

    # Проверяем, что перешли на главную страницу "Дзен"
    assert "https://dzen.ru/?yredirect=true" in driver.current_url

    print("Test for Yandex logo redirect passed successfully.")


test_yandex_logo_redirect()