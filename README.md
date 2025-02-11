# Carsandbids.com Scrapers

## Description

This repository contains Python-based scrapers for Carsandbids.com search results and product pages. These scrapers leverage the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to handle JavaScript rendering, CAPTCHA challenges, and anti-bot protections. The extracted data is processed using BeautifulSoup for HTML parsing and Pandas for structured storage.

➡ Read the full blog [here](https://crawlbase.com/blog/scrape-carsandbids/) to learn more.

## Scrapers Overview

### Carsandbids.com Search Results Scraper

The Carsandbids.com Search Results Scraper (carsandbids_serp_scraper.py) extracts:

1. **Product Name**
2. **Subtitle**
3. **Auction Location**
4. **Thumbnail**
5. **Product Page Link**

It also automatically handles pagination, ensuring comprehensive data extraction. It saves the extracted data in a JSON file.

### Carsandbids.com Product Page Scraper

The Carsandbids.com Product Page Scraper (carsandbids_product_page_scraper.py) extracts detailed car information, including:

1. **Auction Title**
2. **Vehicle Description**
3. **Image Gallery**
4. **Current Bid**
5. **Bid History**
6. **Seller Information**

It saves the extracted data in a JSON file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if you're on Linux with Python 3 installed
python --version
```

Next, install the required dependencies:

```bash
pip install crawlbase beautifulsoup4
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **BeautifulSoup** – Parses and extracts structured data from HTML.

## Running the Scrapers

1. **Get Your Crawlbase Access Token**

   - Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
   - Use the JS token for Carsandbids.com scraping, as the site uses JavaScript-rendered content.

2. **Update the Scraper with Your Token**

   - Replace `"CRAWLBASE_JS_TOKEN"` in the script with your Crawlbase JS Token.

3. **Run the Scraper**

```bash
# Use python3 if required (for Linux/macOS)
python SCRAPER_FILE_NAME.py
```

Replace `"SCRAPER_FILE_NAME.py"` with the actual script name (`carsandbids_serp_scraper.py` or `carsandbids_product_page_scraper.py`).

## To-Do List

- Expand scrapers to extract additional product details.
- Optimize data storage and export formats (e.g., JSON, database integration).
- Enhance scraper efficiency and speed.

## Why Use This Scraper?

- **Bypasses anti-bot protections** with Crawlbase.
- **Handles JavaScript-rendered content** seamlessly.
- **Extracts accurate and structured product data** efficiently.
