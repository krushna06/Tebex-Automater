from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = ""
password = ""

driver_path = r"C:\Users\Administrator\Downloads\tebex-automate\msedgedriver.exe"
service = Service(driver_path)

driver = webdriver.Edge(service=service)

try:
    driver.get("https://accounts.tebex.io/login")

    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys(email)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")))
    login_button.click()

    wait.until(EC.url_changes("https://accounts.tebex.io/login"))

    driver.get("https://creator.tebex.io/packages/create")

    wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Air")
    driver.find_element(By.NAME, "price").send_keys("1.99")
    driver.find_element(By.NAME, "description").send_keys("Display Air tag besides your username.")
    driver.find_element(By.NAME, "commands[0]").send_keys("lp user username permission set supremetags.tag.tagname true")

    from selenium.webdriver.support.ui import Select

    category_dropdown = Select(driver.find_element(By.NAME, "category_id"))
    category_dropdown.select_by_visible_text("Tags > Chats tags")

    server_dropdown = Select(driver.find_element(By.NAME, "server_id"))
    server_dropdown.select_by_visible_text("Proy")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Package creation completed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()