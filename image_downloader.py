from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import os
import time

# Set up the Selenium WebDriver
service = Service('/Users/huynhnhi/Documents/chromedriver-mac-arm64/chromedriver')  # Update this path
driver = webdriver.Chrome(service=service)

def download_images_from_chapter(chapter_url, chapter_folder):
    # Load the chapter page
    driver.get(chapter_url)
    driver.maximize_window()

    # Scroll down to load all images
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Adjust the sleep time as necessary
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Parse the fully loaded page with BeautifulSoup
    chapter_soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all image elements
    images = chapter_soup.find_all('img', class_='chapter_content')
    image_count = len(images)
    
    print(f'Found {image_count} images in {chapter_url}')

    # Download all images
    for index, img in enumerate(images):
        img_url = img['src']
        img_data = None
        try:
            img_data = requests.get(img_url).content
        except requests.exceptions.RequestException as e:
            print(f'Error downloading {img_url}: {e}')
            continue

        # Save the image
        img_name = f'{chapter_folder}/{index + 1}.jpg'
        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)

        print(f'Downloaded {img_name}')
    
    # Verification step
    downloaded_files = os.listdir(chapter_folder)
    if len(downloaded_files) == image_count:
        print(f"All {image_count} images successfully downloaded.")
    else:
        print(f"Warning: Expected {image_count} images, but only {len(downloaded_files)} were downloaded.")

# Example usage
chapter_url = 'https://truyenqqto.com/truyen-tranh/nguoi-di-dem-15534-chap-2.html'
chapter_title = '12424.html'
chapter_folder = f'./{chapter_title}/'

if not os.path.exists(chapter_folder):
    os.makedirs(chapter_folder)

download_images_from_chapter(chapter_url, chapter_folder)

# Close the browser
driver.quit()
