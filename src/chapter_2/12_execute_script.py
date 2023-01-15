from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
        browser = webdriver.Chrome()
        browser.get("http://SunInJuly.github.io/execute_script.html")

        x = browser.find_element(By.ID, "input_value").text
        
        select = browser.find_element(By.ID, "answer")
        select.send_keys(calc(x))
        browser.find_element(By.ID, "robotCheckbox").click()

        button = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        browser.find_element(By.ID, "robotsRule").click()
        button.click()

except:
    print(f"error, mom")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
