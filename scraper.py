import requests
from PIL import Image
from io import BytesIO
import os

# Your Pexels API Key
PEXELS_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
HEADERS = {"Authorization": PEXELS_API_KEY}

# Directory to save images
SAVE_DIR = "D:/DL PROJECT/Vintage_Images"
os.makedirs(SAVE_DIR, exist_ok=True)

# Search keywords for vintage-style low-quality images
# retro portrait", "old photo", "vintage", "sepia", "black and white","lamdscape","grainy", "faded colors", "retro style", "old-fashioned","sepia tone",
KEYWORDS = ["city", "people", "animals", "food", "travel", "art", "music", "fashion"]
PER_PAGE = 100  # Max per request (Pexels allows up to 80 per_page if approved)
MAX_PAGES = 100

image_count = 0

for keyword in KEYWORDS:
    print(f"🔍 Searching for: {keyword}")
    for page in range(1, MAX_PAGES + 1):
        url = f"https://api.pexels.com/v1/search?query={keyword}&per_page={PER_PAGE}&page={page}"
        response = requests.get(url, headers=HEADERS)

        try:
            data = response.json()
            photos = data.get("photos", [])
            if not photos:
                print(f" No results for page {page} on keyword '{keyword}'")
                break

            for i, photo in enumerate(photos):
                img_url = photo["src"]["original"]
                img_data = requests.get(img_url).content
                img = Image.open(BytesIO(img_data)).convert("RGB")
                save_path = os.path.join(SAVE_DIR, f"{keyword.replace(' ', '_')}_{page}_{i}.jpg")
                img.save(save_path, "JPEG", quality=6)
                image_count += 1

        except Exception as e:
            print(f" Error on page {page}: {e}")

print(f"\n🎉 Done! {image_count} images saved to '{SAVE_DIR}'")
