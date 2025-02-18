from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TensorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.driver.get("https://tensor.ru/")
        return self

    def open_details(self):
        details = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[text()='Подробнее']")))[2]
        details.click()
        return self

    def open_about(self):
        self.driver.get("https://tensor.ru/about")
        return self
