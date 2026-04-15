# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import time
#
# def get_driver():
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         return driver
#
# def test_forgot_password():
#     driver = get_driver()
#
#     driver.get("https://the-internet.herokuapp.com/forgot_password")
#     time.sleep(2)
#
#     driver.find_element(By.ID, "email").send_keys("manu143@gmail.com")
#
#     driver.find_element(By.ID, "form_submit").click()
#     time.sleep(2)
#
#     success = driver.find_element(By.TAG_NAME, "h1").text
#
#     assert "Internal server error" or "Email sent" in success
#
#     print("Test passed")
#
#     driver.quit()
#
# # def test_forgot_password_invalid_email():
# #     driver = get_driver()
# #     driver.get("https://the-internet.herokuapp.com/forgot_password")
# #
# #     driver.find_element(By.LINK_TEXT, "Signup / Login").click()
# #     driver.find_element(By.XPATH, "//a[text()='Forgot your password?']").click()
# #
# #     driver.find_element(By.ID, "email").send_keys("invalid@email")
# #     driver.find_element(By.XPATH, "//button[text()='Submit']").click()
# #
# #     error_msg = driver.find_element(By.XPATH, "//div[contains(text(), 'alert-danger')]").text
# #
# #     assert "alert-danger" in error_msg.lower()
# #
# #     driver.quit()