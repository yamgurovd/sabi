from telnetlib import EC

from selenium.webdriver.common.by import By

from pages.saby_page import BasePage


def test_saby_to_tensor_navigation(driver):
    saby_page = BasePage(driver)
    tensor_page = (saby_page
                  .navigate()
                  .open_contacts()
                  .show_more_offices()
                  .open_tensor_site()
                  .navigate())


    assert tensor_page.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Сила в людях']")))


    tensor_page.open_details()
    assert tensor_page.driver.current_url == "https://tensor.ru/about"


    images = tensor_page.driver.find_elements(By.CSS_SELECTOR, '.tensor_ru-About__block3-image img')
    first_height = images[0].get_attribute('height')
    first_width = images[0].get_attribute('width')

    for img in images[1:]:
        assert img.get_attribute('height') == first_height
        assert img.get_attribute('width') == first_width