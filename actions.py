from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from xpaths import xpaths

def click_element(driver, path):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, path))).click()

def wait_for_image_to_load(driver):
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH, xpaths['image_loading_bar'])))

def get_urls(driver, amount):
    image_urls = []
    image_load_fail_count = 0
    max_tries = 5
    while(amount > 0):
        wait_for_image_to_load(driver)
        image_url = driver.find_element(By.XPATH, xpaths['staged_image']).get_attribute('src')
        while(image_url[0:5] != 'https' and image_load_fail_count < max_tries):
            time.sleep(0.2)
            image_url = driver.find_element(By.XPATH, xpaths['staged_image']).get_attribute('src')
            image_load_fail_count += 1
        if(image_url[0:5] == 'https'):
            image_urls.append(image_url)
            amount -= 1
        click_element(driver, xpaths['next_image'])
    return image_urls