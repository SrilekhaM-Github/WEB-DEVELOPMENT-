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
Method 1: Close all tabs except the current one

from selenium import webdriver

# Open a new browser window with multiple tabs
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.execute_script("window.open('https://www.bing.com');")
driver.execute_script("window.open('https://www.yahoo.com');")

# Get the current window handle
current_window_handle = driver.current_window_handle

# Close all tabs except the current one
for window_handle in driver.window_handles:
    if window_handle != current_window_handle:
        driver.switch_to.window(window_handle)
        driver.close()

# Switch back to the original tab
driver.switch_to.window(current_window_handle)

2.Close a specific tab by its index

# Close the second tab (index 1)
driver.switch_to.window(driver.window_handles[1])
driver.close()

# Switch back to the original tab
driver.switch_to.window(driver.window_handles[0])

Close all tabs and open a new one

# Close all tabs
for window_handle in driver.window_handles:
    driver.switch_to.window(window_handle)
    driver.close()

# Open a new tab
driver.get("https://www.duckduckgo.com")
