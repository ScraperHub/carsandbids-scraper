import json
from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({ 'token': 'CRAWLBASE_JS_TOKEN' })

# Function to make a request using Crawlbase API
def make_crawlbase_request(url, options):
    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
      html_content = response['body'].decode('utf-8')
      return html_content
    else:
      print(f"Failed to fetch the page. Crawlbase status code: {response['headers']['pc_status']}")
      return None

# Function to scrape the product page
def scrape_product_page(url, options):
    product_page_html = make_crawlbase_request(url, options)
    if product_page_html:
        soup = BeautifulSoup(product_page_html, 'html.parser')

        title_price_tag = soup.select_one('div.auction-title > h1')

        vehicle_description = {}
        quick_facts = soup.find('div', class_='quick-facts')

        if quick_facts:
            for dl in quick_facts.find_all('dl'):
                for dt, dd in zip(dl.find_all('dt'), dl.find_all('dd')):
                    key = dt.text.strip()
                    value = dd.text.strip() if dd else None
                    vehicle_description[key] = value

        image_gallery = {
            "interior_images": [img['src'] for img in soup.select('div[class*="gall-int"] > img')],
            "exterior_images": [img['src'] for img in soup.select('div[class*="gall-ext"] > img')]
        }

        current_bid_tag = soup.select_one('div.current-bid > div.bid-value')
        bid_history = [bid.text.strip() for bid in soup.select('.comments dl.placed-bid')]

        seller_info_link = soup.select_one('ul.stats li.seller div.username a')
        seller_info = {
            'username': seller_info_link['title'] if seller_info_link else None,
            'profile': 'https://carsandbids.com' + seller_info_link['href'] if seller_info_link else None,
        }

        product_data = {
            'auction_title': title_price_tag.text.strip() if title_price_tag else None,
            'vehicle_description': vehicle_description,
            'image_gallery': image_gallery,
            'current_bid': current_bid_tag.text.strip() if current_bid_tag else None,
            'bid_history': bid_history,
            'seller_info': seller_info
        }

        return product_data
    else:
        print("No data to parse.")

def save_data_as_json(data, output_file):
  with open(output_file, 'w') as file:
      json.dump(data, file, indent=2)

  print(f"Data saved to {output_file}")

# Main function to run the script
def main():
    PRODUCT_PAGE_URL = 'https://carsandbids.com/auctions/9QxJ8nV7/2014-bmw-335i-sedan'
    OUTPUT_FILE = 'product_data.json'
    options = {
    'ajax_wait': 'true',
    'page_wait': 10000
    }

    scraped_data = scrape_product_page(PRODUCT_PAGE_URL, options)
    save_data_as_json(scraped_data, OUTPUT_FILE)

if __name__ == '__main__':
    main()