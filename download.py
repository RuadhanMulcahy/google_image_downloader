from email.mime import image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import PIL.Image as Image

from actions import click_element, get_urls
from config import config
from xpaths import xpaths

def download_images(image_urls, image_folder_path):
    for index, image_url in enumerate(image_urls):
        # image = PIL.Image.open(BytesIO(requests.get(image_url).content))
        response = requests.get(image_url)
        try:
            image = Image.open(BytesIO(response.content))
            image.verify()
            image.close()
            image = Image.open(BytesIO(response.content))
            image.save(f'{image_folder_path}/{index}.png')
        except (IOError, SyntaxError) as e:
            pass

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
image_urls = get_urls(driver, config['amount'])
download_images(image_urls, config['image_folder_path'])
