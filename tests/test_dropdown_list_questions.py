def test_dropdown_list_questions():
    # Открываем главную страницу
    driver.get("https://qa-scooter.praktikum-services.ru/")

    # Подтверждаем использование куки
    cookie_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_CONFIRM_BUTTON))
    cookie_button.click()

    # Проверяем каждый вопрос по отдельности
    questions = [
        (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_TO_THE_QUESTION_1),
        (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_TO_THE_QUESTION_2),
        (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_TO_THE_QUESTION_3),
        (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_TO_THE_QUESTION_4),
        (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_TO_THE_QUESTION_5),
        (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_TO_THE_QUESTION_6),
        (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_TO_THE_QUESTION_7),
        (MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_TO_THE_QUESTION_8)
    ]

    for question, answer in questions:
        question_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(question))
        question_element.click()

        answer_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(answer))
        assert answer_element.is_displayed()

        question_element.click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(answer))

    print("Test for dropdown list questions passed successfully.")


test_dropdown_list_questions()