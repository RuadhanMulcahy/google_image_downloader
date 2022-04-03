from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re

from actions import _click_element
from config import config

driver_location = "/snap/bin/chromium.chromedriver"
binary_location = "/usr/bin/chromium-browser"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.set_window_position(-1000, 0)
driver.maximize_window()

keyword = config['keyword'] 
image_size = config['image_size']
driver.get(f'https://www.google.com/search?q={keyword}+{image_size}&tbm=isch')

# _click_element(driver, '//*[@id="L2AGLb"]')
_click_element(driver, '//*[@id="islrg"]/div[1]/div[1]')


image_url = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]').get_attribute('href')

# image_url = re.split('%2F|&',image_url)
# print(full_split)
image_url = '/'.join(re.split('%2F|&',image_url)[2:5])
driver.get(f'https://{image_url}')
element = driver.find_element(By.XPATH, '/html/body/img')
img = element.screenshot('test.jpg')

# //*[@id="islrg"]/div[1]/div[9]/a[1]
