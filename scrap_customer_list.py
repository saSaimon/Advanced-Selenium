from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from time import sleep
email = "sadiqul@careerist.com"
password = "Sqa@#0987654321"
login_url = "https://backoffice.careerist.com/"
customer_url= "https://backoffice.careerist.com/customers?page=0&perPage=500"

driver = webdriver.Chrome()
driver.maximize_window()
actions = ActionChains(driver)

driver.get(login_url)
driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '[type="button"]').click()

sleep(10)
# driver.get(customer_url)
driver.find_element(By.XPATH, '//div[@class="MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button"][4]').click()
driver.find_element(By.XPATH, "//p[normalize-space()='Customers List']").click()
driver.find_element(By.CSS_SELECTOR, '#mui-57368').click()

driver.find_element(By.CSS_SELECTOR, 'li:nth-child(6)').click()
sleep(15)
# actions.move_by_offset(1200, 200).click().perform()


element_export = driver.find_element(By.CSS_SELECTOR, '#mui-79645')
element_next_button = driver.find_element(By.CSS_SELECTOR, "div[aria-label='grid'] div div div[class='MuiDataGrid-toolbar'] button[title='Next page'] span[class='MuiIconButton-label'] svg")



for i in range(1,1679):
    element_export.click()
    sleep(5)
    element_next_button.click()
    sleep(10)

