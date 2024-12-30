import os
import requests
from bs4 import BeautifulSoup

# URL of the comic chapter
url = 'https://truyenqqto.com/truyen-tranh/nguoi-di-dem-15534-chap-4.html'

# Directory to save images
save_dir = 'comic_images4'
os.makedirs(save_dir, exist_ok=True)

# Fetch the webpage content
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36',
}
response = requests.get(url, headers=headers)
response.raise_for_status()

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image containers
image_containers = soup.find_all('div', class_='page-chapter')

# Download each image
for idx, container in enumerate(image_containers, start=1):
    img_tag = container.find('img')
    if img_tag and img_tag.get('src'):
        img_url = img_tag['src']
        # Add a referer header to mimic the request's origin
        img_headers = {
            'User-Agent': headers['User-Agent'],
            'Referer': url  # This mimics the referer from the main webpage
        }
        img_response = requests.get(img_url, headers=img_headers)
        img_response.raise_for_status()
        # Determine the image extension
        ext = img_url.split('.')[-1].split('?')[0]
        img_filename = f'comic_page_{idx:03d}.{ext}'
        img_path = os.path.join(save_dir, img_filename)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_response.content)
        print(f'Downloaded {img_filename}')
