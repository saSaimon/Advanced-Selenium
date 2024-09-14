import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variables
login_url = "https://testtalents.com/auth/login"
reg_url = 'https://testtalents.com/auth/register'
email = 'sadiqul@careerist.com'
password = 'Saimon@#098'
# Set up the WebDriver (replace with your preferred browser)
driver = webdriver.Chrome()

# Navigate to the login page
driver.get(login_url)

# Find and enter username and password
email_field = driver.find_element(By.CSS_SELECTOR, "#recruiterLoginEmail")  # Replace with the actual ID
email_field.send_keys(email)
password_field = driver.find_element(By.CSS_SELECTOR, "#recruiterLoginPassword")  # Replace with the actual ID
password_field.send_keys(password)

# Click the login button
login_button = driver.find_element(By.CSS_SELECTOR, "#recruiterLoginFormButton")  # Replace with the actual XPath
login_button.click()

# Verify successful login (adjust the locator as needed)
try:
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='sidebar-logout'] span[class='ml-16']")))
    print("Login successful!")
except:
    print("Login failed!")

time.sleep(10)
#Navigate to the registration page
# driver.get(reg_url)
#
# # Fill in registration form
# full_name = driver.find_element(By.CSS_SELECTOR, "#recruiterRegisterFullName")  # Replace with the actual ID
# full_name.send_keys("new_user")
# email_field = driver.find_element(By.CSS_SELECTOR, "#recruiterRegisterEmail")  # Replace with the actual ID
# email_field.send_keys("new_user@example.com")
# password_field = driver.find_element(By.CSS_SELECTOR, "#recruiterRegisterPassword")  # Replace with the actual ID
# password_field.send_keys("your_password")
# # Add other required fields as needed
#
# # Click the register button
# Sign_up_button = driver.find_element(By.CSS_SELECTOR, "#recruiterRegisterFormButton")  # Replace with the actual XPath
# Sign_up_button.click()
#
# # Verify successful registration (adjust the locator as needed)
# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SEECTOR, '[href="/dashboard/my-profile"]')))
#     print("Registration successful!")
# except:
#     print("Registration failed!")
#
# # Close the browser
# driver.quit()
