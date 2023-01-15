from selenium import webdriver
from selenium.webdriver.common.by import By
import time

links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]

try: 
    for link in links:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your last name\"]")
        input3.send_keys("Petrov")
        input4 = browser.find_element(By.CSS_SELECTOR, "[placeholder=\"Input your email\"]")
        input4.send_keys("Russia")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
except:
    print(f"error in {link}")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
