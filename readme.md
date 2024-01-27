# Fake Job Listings Web Scraper

This Python script demonstrates web scraping using the `requests` and `BeautifulSoup` libraries to extract fake job listings from a sample webpage. The webpage used for scraping is "https://realpython.github.io/fake-jobs/".

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- Required Python packages (`requests` and `beautifulsoup4`)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Installation
1. Clone the repository:

```
git clone https://github.com/Cronic7/beautifulsoup-tutorial.git
cd beautifulsoup-tutorial

```
2. Install dependencies:
```
pip install -r requirements.txt

```
## Usage

Run the Python script:
```
python beautifulSoup.py

```
## Tutorial and Explanation

The script performs the following tasks:

1. Sends an HTTP GET request to the specified URL.
2. Parses the HTML content of the webpage using BeautifulSoup.
3. Finds the container element with the ID "ResultsContainer" that holds the job listings.
4. Extracts job listings by finding all `<div>` elements with the class "card-content" within the container.
5. For each job listing, extracts and prints the job title, company name, and location.

Feel free to customize the script according to your needs and explore additional features provided by BeautifulSoup for web scraping.

## Notes

- The script uses a sample webpage for demonstration purposes. Make sure to respect the terms of use of any website you choose to scrape.
- Ensure you have permission to scrape data from the target website, and be mindful of their robots.txt file.

## Author

Cronic7


