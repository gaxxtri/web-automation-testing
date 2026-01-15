from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def test_amazon_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.amazon.in/")
    time.sleep(3)
    assert "Amazon" in driver.title
    
    box = driver.find_element(By.ID, "twotabsearchtextbox")
    box.send_keys("phone")
    box.send_keys(Keys.ENTER)
    time.sleep(3)
    
    items = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium")
    assert len(items) > 0
    
    driver.quit()
