import requests

def check_headers(url):
    # Use a browser-like header
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Send request to get response headers
        response = requests.get(url, headers=headers, timeout=10)
    except requests.RequestException as e:
        print("Error loading page:", e)
        return

    print(f"\n--- Security Header Report for {url} ---\n")

    # Common security headers to check
    security_headers = {
        "Content-Security-Policy": "Prevents malicious scripts (XSS protection)",
        "X-Frame-Options": "Prevents clickjacking",
        "Strict-Transport-Security": "Forces HTTPS (HSTS)",
        "X-Content-Type-Options": "Prevents MIME sniffing",
        "Referrer-Policy": "Controls referrer information",
        "Permissions-Policy": "Restricts browser features"
    }

    found = 0

    for header, description in security_headers.items():
        if header in response.headers:
            print(f"[FOUND] {header}")
            found += 1
        else:
            print(f"[MISSING] {header} → {description}")

    print("\nSummary:")
    print(f"{found} / {len(security_headers)} security headers present")

    # Simple rating
    if found == len(security_headers):
        print("Security Status: STRONG")
    elif found >= 3:
        print("Security Status: MODERATE")
    else:
        print("Security Status: WEAK")


if __name__ == "__main__":
    url = input("Enter URL: ").strip()
    check_headers(url)
