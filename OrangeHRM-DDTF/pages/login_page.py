# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, '//button[@type="submit"]')
        self.error_message = (By.CSS_SELECTOR, '.error-message')

# Using explicit waits to ensure elements are present before interacting with them

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


    def implicitly_wait_for_login(self):
        # Implicitly wait for the login process to complete
        self.driver.implicitly_wait(10).click()
        


    def is_login_successful(self):
        # Assuming no error message means login is successful
        return not WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.error_message)).is_displayed()