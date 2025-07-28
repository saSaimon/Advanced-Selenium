from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


data = {
    "full_name": "John Doe",
    "phone_number": "01700000000",
    "dob": "195-12-01",
    "gender": "Male",
    "email": f"john{int(time.time())}@example.com",  # Unique email each run
    "password": "StrongPass123"
}


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://career.techforing.com/auth/register")
wait = WebDriverWait(driver, 10)


wait.until(EC.presence_of_element_located((By.ID, "fullName"))).send_keys(data["full_name"])
driver.find_element(By.NAME, "phone_number").send_keys(data["phone_number"])
driver.find_element(By.CSS_SELECTOR, 'input[type="date"]').click()
driver.find_element(By.CSS_SELECTOR, ".signup_form_dateofbirth input").send_keys(data["dob"])
driver.find_element(By.XPATH, "//label[text()='Gender']/following-sibling::div").click()
wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[text()='{data['gender']}']"))).click()
driver.find_element(By.NAME, "email").send_keys(data["email"])
driver.find_element(By.NAME, "password").send_keys(data["password"])
driver.find_element(By.NAME, "confirm_password").send_keys(data["password"])


input("✅ Solve CAPTCHA manually and press ENTER to continue...")
time.sleep(10)

submit_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@type='submit'")
))
submit_btn.click()




