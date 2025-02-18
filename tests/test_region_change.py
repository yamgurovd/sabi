from telnetlib import EC

from selenium.webdriver.common.by import By

from pages.saby_page import BasePage


def test_region_change(driver):
    saby_page = BasePage(driver)

    saby_page.navigate().open_contacts()

    assert saby_page.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='г. Санкт-Петербург']")))
    assert saby_page.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Список партнеров']")))

    saby_page.show_more_offices().open_kamchatka_office()

    assert saby_page.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Камчатский край']")))
    assert saby_page.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Saby - Камчатка']")))
    assert "kamchatka" in saby_page.driver.current_url
    assert "Камчатка" in saby_page.driver.title
