from email.mime import image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import requests
import time

from actions import click_element, get_urls
from config import config
from xpaths import xpaths

def download_images(image_urls, image_folder_path):
    for index, image_url in enumerate(image_urls):
        img_data = requests.get(image_url).content
        site_name = image_url.split('/')[0]
        file_name = f'{site_name}_{index}.png'
        with open(f'{image_folder_path}/{file_name}', 'wb') as handler:
            handler.write(img_data)

driver_location = "/snap/bin/chromium.chromedriver"
binary_location = "/usr/bin/chromium-browser"

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--headless")
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.set_window_position(-1000, 0)
driver.maximize_window()

keyword = config['keyword'] 
image_size = config['image_size']
driver.get(f'https://www.google.com/search?q={keyword}+imagesize:{image_size}&tbm=isch')

click_element(driver, xpaths['first_thumbnail_image'])
image_urls = get_urls(driver, 10)
print(image_urls)
print(len(image_urls))
download_images(image_urls, config['image_folder_path'])