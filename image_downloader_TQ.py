import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the webpage
webpage_url = "https://truyenqqto.com/truyen-tranh/nguoi-di-dem-15534-chap-2.html"
output_folder = "downloaded_comics2"

# Create folder to store images
os.makedirs(output_folder, exist_ok=True)

# Function to download an image
def download_image(img_url, output_folder, img_order):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
        }
        response = requests.get(img_url, headers=headers, stream=True)
        response.raise_for_status()
        
        # Extract file extension
        ext = img_url.split("wx_fmt=")[-1].split("&")[0] if "wx_fmt=" in img_url else "jpg"
        filename = f"comic_{img_order:03d}.{ext}"  # Zero-padded order for sorting
        filepath = os.path.join(output_folder, filename)

        # Save the image
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")

# Function to extract and preserve the sequence of comic image URLs
def extract_comic_image_urls(webpage_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }
    response = requests.get(webpage_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    img_urls = []

    # Look for the `article-content` class
    article_content = soup.find(class_="article-content")
    if article_content:
        # Find all <img> tags within `article-content` in order
        for img in article_content.find_all("img"):
            src = img.get("src")
            if src and "mmbiz.qpic.cn" in src:  # Filter for images hosted on mmbiz.qpic.cn
                img_urls.append(urljoin(webpage_url, src))
    
    return img_urls

# Main process
def main():
    # Extract comic image URLs
    print("Extracting comic image URLs from 'article-content'...")
    img_urls = extract_comic_image_urls(webpage_url)
    print(f"Found {len(img_urls)} comic image URLs.")

    # Download each image in sequence
    for order, img_url in enumerate(img_urls, start=1):
        download_image(img_url, output_folder, order)

if __name__ == "__main__":
    main()
