from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_details(self):
        self.driver.find_element(By.ID, "first-name").send_keys("Manu")
        self.driver.find_element(By.ID, "last-name").send_keys("Kamma")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")

        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_btn.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-two")
        )

    def finish_order(self):
        finish_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        finish_btn.click()

    def get_success_message(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        return element.text