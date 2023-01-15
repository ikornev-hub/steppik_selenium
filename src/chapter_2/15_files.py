from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
assets_path = os.path.abspath("assets")

try:
  browser = webdriver.Chrome()
  browser.get(link)

  for field in browser.find_elements(By.CSS_SELECTOR, "input[type=\"text\"]"):
    field.send_keys("something")

  file_txt = os.path.join(assets_path, "empty_file.txt")
  browser.find_element(By.ID, "file").send_keys(file_txt)

  browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"").click()

finally:
  time.sleep(10) 
  browser.quit()