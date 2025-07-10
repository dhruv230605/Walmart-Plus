# scrapers/amazon_best_sellers.py
import requests
from bs4 import BeautifulSoup

def fetch_amazon_best_sellers(url='https://www.amazon.com/Best-Sellers/zgbs'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Placeholder: parse product names
    products = [item.text for item in soup.select('.p13n-sc-truncate')]
    return products 