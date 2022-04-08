from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import requests
import time

from actions import _click_element
from config import config

def get_urls(driver, amount):
    image_urls = []
    # image_url = driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[1]/a[1]').get_attribute('href')

    for i in range(1, amount):
        image_url = driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]').get_attribute('href')
        image_urls.append('/'.join(re.split('%2F|&',image_url)[2:5]))
        _click_element(driver, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/a[4]')

    return image_urls

    # image_urls.append('/'.join(re.split('%2F|&',image_url)[2:5]))
    # for i in range(0, 10):
    #     # _click_element(driver, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/a[4]')
    #     # driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').screenshot(f'{image_folder_path}/image_{i}.png')
    #     print(driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute('src'))
    #     # image_url = driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{image_num}]/a[1]').get_attribute('href')

    #     # //*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img
    #     # image_urls.append('/'.join(re.split('%2F|&',image_url)[2:5]))

    # print(image_urls)

def download_images(image_urls, image_folder_path):
    for index, image_url in enumerate(image_urls):
        img_data = requests.get(f'https://{image_url}').content
        site_name = image_url.split('/')[0]
        file_name = f'{site_name}_{index}.png'
        with open(f'{image_folder_path}/{file_name}', 'wb') as handler:
            handler.write(img_data)

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

_click_element(driver, f'//*[@id="islrg"]/div[1]/div[1]')
image_urls = get_urls(driver, 30)
download_images(image_urls, config['image_folder_path'])


# image_url = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]').get_attribute('href')

# # image_url = re.split('%2F|&',image_url)
# # print(full_split)
# image_url = '/'.join(re.split('%2F|&',image_url)[2:5])
# # driver.get(f'https://{image_url}')
# # element = driver.find_element(By.XPATH, '/html/body/img')
# # img = element.screenshot('test.jpg')
# img_data = requests.get(f'https://{image_url}').content
# with open('image_name.jpg', 'wb') as handler:
#     handler.write(img_data)

# //*[@id="islrg"]/div[1]/div[9]/a[1]
