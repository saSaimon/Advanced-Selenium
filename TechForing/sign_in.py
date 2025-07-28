from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


data = {

    "email": "johndoe1234@gmail.com",  # Unique email each run
    "password": "StrongPass123"
}

# === Setup Driver ===
driver = webdriver.Chrome()
driver.maximize_window()



driver.get("https://career.techforing.com/auth")
wait = WebDriverWait(driver, 10)


wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(data["email"])
driver.find_element(By.NAME, "password").send_keys(data["password"])
driver.find_element(By.XPATH, "//button[@type='submit']").click()


time.sleep(5)
driver.save_screenshot("signed_in.png")

driver.quit()