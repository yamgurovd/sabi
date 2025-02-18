import os
from telnetlib import EC

from selenium.webdriver.common.by import By

from pages.saby_page import BasePage


def test_plugin_download_plugin_download(driver):
    saby_page = BasePage(driver)

    saby_page.navigate()

    saby_page.open_downloads()

    saby_page.select_saby_plugin()
    download_path = saby_page.download_plugin()

    assert os.path.exists(download_path)

    file_size_mb = os.path.getsize(download_path) / (1024 * 1024)
    size_element = saby_page.wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Скачать (Exe')]")))
    size_on_page = float(size_element.text.split()[2].replace(',', '.'))
    assert abs(file_size_mb - size_on_page) < 0.01
