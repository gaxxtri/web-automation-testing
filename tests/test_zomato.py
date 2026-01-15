from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_zomato_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.zomato.com/chennai")
    time.sleep(5)
    assert "Zomato" in driver.title
    
    wait = WebDriverWait(driver, 20)

    # close popup if present
    try:
        close_btn = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Close']"))
        )
        close_btn.click()
    except:
        pass

    search_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'Search')]"))
    )
    
    search_box.send_keys("pizza")
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)
    
    cards = driver.find_elements(By.CSS_SELECTOR, "div.sc-1hp8d8a-0")
    assert len(cards) > 0  # mark FAIL if no results
    
    driver.quit()
