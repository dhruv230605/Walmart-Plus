import requests
from bs4 import BeautifulSoup
import re
import json

url = "https://www.amazon.in/gp/bestsellers"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.select('div.p13n-sc-uncoverable-faceout')
    data = []

    for i, item in enumerate(items[:10], 1):
        title_tag = item.select_one('._cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
        link_tag = item.find('a', href=True)

        title = title_tag.get_text(strip=True) if title_tag else "No title found"
        link = "https://www.amazon.in" + link_tag['href'] if link_tag else "No link found"

        # Extract readable name from URL
        match = re.search(r'amazon\.in/([^/]+)/dp/', link)
        product_name = match.group(1).replace('-', ' ') if match else title

        data.append({
            "rank": i,
            "product_name": product_name,
            "full_title": title,
            "link": link
        })

    # Save to JSON file
    with open("amazon_bestsellers.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✅ Top 10 products saved to amazon_bestsellers.json")
else:
    print("❌ Failed to fetch the page. Status code:", response.status_code)