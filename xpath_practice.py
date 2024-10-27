from time import sleep
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.atlassian.com/software/jira')
sleep(5)

#parent to child
# driver.find_element(By.XPATH, '//button/span/div/div/span[@class="_ect4q6fz _1wyboxav _syazrbzz"]').click()
#contains xpath
driver.find_element(By.XPATH, ).click()


sleep(5)