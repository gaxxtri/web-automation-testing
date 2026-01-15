from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_openweather_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    driver.get("https://openweathermap.org/")
    time.sleep(4)
    assert "Weather" in driver.title
    
    box = driver.find_element(By.XPATH, "//input[@placeholder='Search city']")
    box.send_keys("Chennai")
    box.send_keys(Keys.ENTER)
    time.sleep(3)
    
    first = driver.find_element(By.CSS_SELECTOR, "ul.search-dropdown-menu li")
    first.click()
    
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "weather-widget__temperature"))
        )
        assert True
    except:
        assert False  # flaky cases count as FAIL
    
    driver.quit()
