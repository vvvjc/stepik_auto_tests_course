import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )
    browser.find_element(By.CSS_SELECTOR, "#book").click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    button2.click()

    print(browser.switch_to.alert.text)


finally:
    browser.quit()
