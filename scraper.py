# scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver

def fetch_data(driver, url, element_id):
    driver.get(url)
    try:
        element = driver.find_element("id", element_id)
        return element.text
    except Exception as e:
        return f"Error: {e}"
