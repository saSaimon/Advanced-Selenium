import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


login_url = "https://www.canvas8.com/"
driver = webdriver.Chrome()

driver.get(login_url)


elements = driver.find_elements(By.XPATH, "//div[contains(@class,'CrossyRoad')]/a/span")
print(len(elements))
count = 0
for element in elements:
    print(element.text)



driver.quit()