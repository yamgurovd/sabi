from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

from pages.tensor_page import TensorPage


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.driver.get("https://saby.ru/?redir=1")
        return self

    def open_contacts(self):
        contacts = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Контакты']")))
        contacts.click()
        return self

    def show_more_offices(self):
        more_offices = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Еще 25 офисов в регионе']")))
        more_offices.click()
        return self

    def open_tensor_site(self):
        main_window = self.driver.current_window_handle
        tensor_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Разработчик системы Saby']")))
        tensor_link.click()

        # Switch to new window
        for window_handle in self.driver.window_handles:
            if window_handle != main_window:
                self.driver.switch_to.window(window_handle)
                break

        return TensorPage(self.driver)

    def open_downloads(self):
        downloads = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Скачать локальные версии']")))
        downloads.click()
        return self

    def select_saby_plugin(self):
        plugin = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Saby Plugin']")))
        plugin.click()
        self.driver.get("https://saby.ru/download?tab=plugin&innerTab=default")
        return self

    def download_plugin(self):
        download_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Скачать (Exe')]")))
        download_link.click()
        # Wait for download to complete
        downloads_path = os.path.expanduser("~/Downloads")
        return os.path.join(downloads_path, "saby_plugin.exe")

    def open_spb_office(self):
        spb_office = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Saby - Санкт-Петербург']")))
        spb_office.click()
        popup = self.wait.until(EC.presence_of_element_located((By.ID, "popup")))
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        return self

    def select_spb(self):
        contacts = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Контакты']")))
        contacts.click()
        spb = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='г. Санкт-Петербург']")))
        spb.click()
        return self

    def open_kamchatka_office(self):
        kamchatka = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Камчатский край']")))
        kamchatka.click()
        office = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Saby - Камчатка']")))
        office.click()
        popup = self.wait.until(EC.presence_of_element_located((By.ID, "popup")))
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        return self
