from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.saucedemo.com/")

    # Логин
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ждём загрузки страницы после логина (достаточно 10 секунд)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    )

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total = total_element.text
    assert "$58.29" in total

    driver.quit()
