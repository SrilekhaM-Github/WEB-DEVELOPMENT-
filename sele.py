from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/")
print(driver.title)
link=driver.find_element(By.LINK_TEXT,"PYTHON")
link.click()
'''
search = driver.find_element(By.ID, "tnb-google-search-input")
search.send_keys("python Tutorial")
search.send_keys(Keys.RETURN)
'''
try:
    # wait 10 seconds before looking for element
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"w3-right w3-btn"))
    )
    element.click()
except:
    # else quit
    driver.quit()
