from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
  browser = webdriver.Chrome()
  browser.get(link)

  browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"").click()

  browser.switch_to.window(browser.window_handles[1])

  x = browser.find_element(By.ID, "input_value").text
        
  browser.find_element(By.ID, "answer").send_keys(calc(x))
  
  browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"").click()

finally:
  time.sleep(10) 
  browser.quit()