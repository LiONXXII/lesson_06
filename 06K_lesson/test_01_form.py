from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


def test_form():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Edge(options=options)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Поле "Zip code" (name="zip-code") оставляем пустым, как в задании
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    driver.execute_script("arguments[0].click();", submit_button)

    zip_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_field.get_attribute("class")

    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    for field_id in fields:
        field = driver.find_element(By.CSS_SELECTOR, f"#{field_id}")
        assert "alert-success" in field.get_attribute("class")

    driver.quit()
