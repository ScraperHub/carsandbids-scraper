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

# Function to scrape search results page
def scrape_search_results_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    car_listings = soup.find_all('li', class_='auction-item')

    extracted_data = []
    for listing in car_listings:
        auction_title = listing.find('div', class_='auction-title').text.strip() if listing.find('div', class_='auction-title') else None
        auction_sub_title = listing.find('p', class_='auction-subtitle').text.strip() if listing.find('p', class_='auction-subtitle') else None
        auction_location = listing.find('p', class_='auction-loc').text.strip() if listing.find('p', class_='auction-loc') else None
        thumbnail = listing.find('img')['src'] if listing.find('img') else None
        product_page_link = 'https://www.carsandbids.com' + listing.find('a')['href'] if listing.find('a') else None

        extracted_data.append({
            'title': auction_title,
            'sub_title': auction_sub_title,
            'auction_location': auction_location,
            'thumbnail': thumbnail,
            'product_page_link': product_page_link
        })
    return extracted_data

# Function to save data to a JSON file
def save_data_as_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    print(f"Data saved to {filename}")

# Main function
def main():
    SEARCH_RESULTS_URL = 'https://carsandbids.com/search/bmw'
    OUTPUT_FILE = 'search_results.json'
    options = {
    'ajax_wait': 'true',
    'page_wait': 10000
    }

    # Fetch the search results page
    search_results_html = make_crawlbase_request(SEARCH_RESULTS_URL, options)

    if search_results_html:
        # Scrape the search results page
        extracted_data = scrape_search_results_page(search_results_html)

        # Save the extracted data to a JSON file
        save_data_as_json(extracted_data, OUTPUT_FILE)
    else:
        print("No data to parse.")

if __name__ == '__main__':
    main()