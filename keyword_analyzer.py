import requests
from bs4 import BeautifulSoup

def analyze_keyword(url, keyword):
    # Use a browser-like header to avoid basic blocking
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Fetch the webpage
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print("Error loading page:", e)
        return

    # Remove script and style elements (not useful for content analysis)
    for tag in soup(["script", "style"]):
        tag.decompose()

    # Get visible text and normalize it
    text = soup.get_text().lower()

    # Count keyword occurrences
    keyword = keyword.lower()
    count = text.count(keyword)

    # Basic output
    print(f"\nKeyword: '{keyword}'")
    print(f"Occurrences: {count}")

    # Simple interpretation
    if count == 0:
        print("Status: NOT FOUND")
    elif count < 5:
        print("Status: LOW USAGE")
    elif count < 15:
        print("Status: GOOD USAGE")
    else:
        print("Status: HIGH USAGE (possible keyword stuffing)")

if __name__ == "__main__":
    url = input("Enter URL: ").strip()
    keyword = input("Enter keyword: ").strip()

    analyze_keyword(url, keyword)
