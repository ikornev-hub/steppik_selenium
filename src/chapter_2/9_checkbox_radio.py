from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/math.html")

        # Ваш код, который заполняет обязательные поля
        x = browser.find_element(By.ID, "input_value").text
        
        input3 = browser.find_element(By.ID, "answer")
        input3.send_keys(calc(x))
        input4 = browser.find_element(By.CSS_SELECTOR, "[for=\"robotCheckbox\"")
        input4.click()
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "[for=\"robotsRule\"]")
        button.click()
        button2 = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
        button2.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
except:
    print(f"error, mom")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
