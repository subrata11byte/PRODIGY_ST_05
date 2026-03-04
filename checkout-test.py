from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open Chrome
driver = webdriver.Chrome()  # or provide path if needed
driver.implicitly_wait(10)

# Step 2: Open SauceDemo
driver.get("https://www.saucedemo.com/")

# Step 3: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print("Login successful")

# Step 4: Add item to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
print("Item added to cart")

# Step 5: Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Step 6: Checkout
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Subrata")
driver.find_element(By.ID, "last-name").send_keys("Roy")
driver.find_element(By.ID, "postal-code").send_keys("700034")
driver.find_element(By.ID, "continue").click()
print("Checkout form submitted")

# Step 7: Finish purchase
driver.find_element(By.ID, "finish").click()

# Step 8: Verify success
success_text = driver.find_element(By.CLASS_NAME, "complete-header").text
assert "THANK YOU" in success_text.upper()
print("Checkout Test Passed!")

# Step 9: Close browser
driver.quit()