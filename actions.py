from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

def click_element(driver, path):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, path))).click()

def wait_for_image_to_load(driver):
    # WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.k7O2sd')))
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/div')))
    time.sleep(0.2)