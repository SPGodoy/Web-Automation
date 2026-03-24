import requests
from bs4 import BeautifulSoup
import argparse

def scrape_metadata(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip() if soup.title else "No title"

    meta = soup.find("meta", attrs={"name": "description"})
    description = meta["content"].strip() if meta and "content" in meta.attrs else "No description"

    h1_tags = [h1.text.strip() for h1 in soup.find_all("h1")]

    print(f"\n--- {url} ---")
    print("Title:", title)
    print("Description:", description)
    print("H1s:", h1_tags if h1_tags else "None")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape metadata from websites")
    
    # accept multiple URLs
    parser.add_argument("urls", nargs="+", help="List of URLs to scrape")

    args = parser.parse_args()

    for url in args.urls:
        scrape_metadata(url)
