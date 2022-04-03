from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def _click_element(driver, path):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, path))).click()

