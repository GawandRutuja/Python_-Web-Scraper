#import Libraries
import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    # Send an HTTP GET request to the specified URL
    response = requests.get('https://github.com/GawandRutuja')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract data from the parsed HTML (example: extracting text from all paragraphs)
        paragraphs = soup.find_all('p')
        extracted_text = [paragraph.get_text() for paragraph in paragraphs]

        # Print or process the extracted data
        for text in extracted_text:
            print(text)
    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")

# Example usage
url_to_scrape = 'https://github.com/GawandRutuja'
simple_web_scraper(url_to_scrape)
