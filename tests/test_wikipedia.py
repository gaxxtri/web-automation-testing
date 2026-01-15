from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def test_wikipedia_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://www.wikipedia.org/")
    time.sleep(2)
    assert "Wikipedia" in driver.title
    
    box = driver.find_element(By.ID, "searchInput")
    box.send_keys("India")
    box.send_keys(Keys.ENTER)
    time.sleep(2)
    
    assert "India" in driver.title
    
    driver.quit()

