import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

email = "sadiqul@careerist.com"
password = "Sqa@#0987654321"
login_url = "https://backoffice.careerist.com/"
customer_url = "https://backoffice.careerist.com/customers?page=0&perPage=500"

driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Log in
driver.get(login_url)
driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '[type="button"]').click()

# Step 2: Wait for any potential overlays to disappear
sleep(5)  # May need to adjust this based on your application's speed

# Step 3: Navigate to customer URL
driver.get(customer_url)

# Step 4: Wait for the sidebar to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="MuiPaper-root MuiDrawer-paper MuiDrawer-paperAnchorLeft MuiPaper-elevation16"]')))
time.sleep(10)
# Step 5: Close the sidebar if it is open
try:
    # Here, we assume that clicking on the sidebar will close it
    sidebar = driver.find_element(By.CSS_SELECTOR, '[class="MuiPaper-root MuiDrawer-paper MuiDrawer-paperAnchorLeft MuiPaper-elevation16"]')

    # If there's a button or an area to click to close it, you would use that
    # If clicking on the sidebar itself closes it, uncomment the line below
    # sidebar.click()

    # Alternatively, you might need to perform an action on the page to close it
    actions = ActionChains(driver)
    actions.move_to_element(sidebar).move_by_offset(0, -100).click().perform()  # Adjust the offset if needed
except Exception as e:
    print(f"Error closing sidebar: {e}")


# Wait for "Customers List" to be visible and click it
try:
    customers_list = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Customers List']"))  # Update this XPath based on the actual HTML structure
    )
    customers_list.click()
except Exception as e:
    print(f"Error clicking Customers List: {e}")
# Step 6: Wait for the sidebar to close (if necessary)
sleep(5)  # Wait for the sidebar to close

# Step 7: Attempt to click on the search input
# try:
#     search_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Search by name, email, phone"]')
#     search_input.click()
# except Exception as e:
#     print(f"An error occurred while clicking the search input: {e}")
#     # JavaScript click as a fallback
#     driver.execute_script("arguments[0].click();", search_input)

# Step 8: Proceed with the rest of your code
# element_export = driver.find_element(By.CSS_SELECTOR, '#mui-79645')
# element_next_button = driver.find_element(By.CSS_SELECTOR,
#                                           "div[aria-label='grid'] div div div[class='MuiDataGrid-toolbar'] button[title='Next page'] span[class='MuiIconButton-label'] svg")
#
# for i in range(1, 1679):
#     element_export.click()
#     sleep(5)
#     element_next_button.click()
#     sleep(10)

# Close the browser
driver.quit()
