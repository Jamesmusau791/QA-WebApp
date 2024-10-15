from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Navigate to Album page
driver.get("http://localhost:3000/albums")

# Search for an album
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Sample Album" + Keys.RETURN)

assert "Sample Album" in driver.page_source
print("Search test passed.")

driver.quit()
