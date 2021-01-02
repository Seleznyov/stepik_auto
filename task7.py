from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element_by_id("book")
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
if price == True:
    button.click()

val = browser.find_element_by_css_selector("[id='input_value']").text
result = calc(val)

Rule = browser.find_element_by_css_selector("[class='btn btn-primary']")
browser.execute_script("return arguments[0].scrollIntoView(true);", Rule)

browser.find_element_by_css_selector("[id='answer']").send_keys(result)
browser.find_element_by_id("solve").click()

al = browser.switch_to.alert.text
print(al)
browser.quit()