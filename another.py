from selenium import webdriver

def close_specific_tab(driver, tab_index):
    """
    Close a specific tab and return to the original tab.

    :param driver: Selenium WebDriver instance
    :param tab_index: Index of the tab to close (0-based)
    :return: None
    """
    # Get the current window handle
    original_window_handle = driver.current_window_handle

    # Get the list of window handles
    window_handles = driver.window_handles

    # Check if the tab index is valid
    if tab_index < 0 or tab_index >= len(window_handles):
        raise ValueError("Invalid tab index")

    # Switch to the tab to close
    driver.switch_to.window(window_handles[tab_index])

    # Close the tab
    driver.close()

    # Switch back to the original tab
    driver.switch_to.window(original_window_handle)

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.execute_script("window.open('https://www.bing.com');")
driver.execute_script("window.open('https://www.yahoo.com');")

# Close the second tab (index 1)
close_specific_tab(driver, 1)