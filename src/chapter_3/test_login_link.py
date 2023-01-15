import time 
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('links', [
  "https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1",
])
def test_login2(browser, links):
  link = f"{links}"
  browser.get(link)
  
  login_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "ember33"))
    )  
  login_button.click()  
  browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("aferistus48@gmail.com")
  browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("Proletarism48")
  browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
  time.sleep(8)
  answer = math.log(int(time.time()))
  browser.find_element(By.CSS_SELECTOR, "[spellcheck=\"false\"]").send_keys(answer) 
  print("Запись в ответ")
  submnit_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
  submnit_button.click()
  assert "Correct!" == browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
  print("клик по ")
