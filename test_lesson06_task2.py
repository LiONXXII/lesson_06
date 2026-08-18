from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # Cookie для пользователя 1
    user1_cookie = {
        "name": "sessionid",
        "value": ("3:1785965143.5.0.1778008756297:3W5MUA:8ef4.1.2:1|"
                  "643407306.-1.20002.3:1778008756.6:2157719545.7:1778008756|"
                  "3:12092730.19228.z7C58J8sCKJ6gvtEZc2vQGs4m2k"),
        "domain": "gitflic.ru"
    }

    # Cookie для пользователя 2
    user2_cookie = {
        "name": "sessionid",
        "value": ("3:1786974666.5.0.1783956973878:3W5MUA:d7c6.1.2:1|"
                  "643407306.-1.20002.3:1783956973|"
                  "3:12119628.826153.Pw-t_GM9eO58AxWwuFG9L7PC6kY"),
        "domain": "gitflic.ru"
    }

    # 1. Открыть страницу
    driver.get("https://gitflic.ru/")

    # 2. Установить cookie пользователя 1
    driver.add_cookie(user1_cookie)

    # 3. Обновить страницу
    driver.refresh()

    # 4. Перейти на страницу пользователя 1
    driver.get("https://gitflic.ru/user/lionxxii")
    url1 = driver.current_url

    # 5. Разлогиниться (очистить cookies)
    driver.delete_all_cookies()

    # 6. Установить cookie пользователя 2
    driver.add_cookie(user2_cookie)

    # 7. Обновить страницу
    driver.refresh()

    # 8. Перейти на страницу пользователя 2
    driver.get("https://gitflic.ru/user/lionxxvi")
    url2 = driver.current_url

    # 9. Проверить, что URL разные
    assert url1 != url2

    driver.quit() # Комментарии излишни
