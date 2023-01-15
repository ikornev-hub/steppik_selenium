from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/selects1.html")

        x = browser.find_element(By.ID, "num1").text
        y = browser.find_element(By.ID, "num2").text
        select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
        select.select_by_value(str(int(x) + int(y)))
        button = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
        button.click()

except:
    print(f"error, mom")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
