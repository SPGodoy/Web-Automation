import requests
import time
import argparse

def check_speed(url):
    # Use a browser-like header to avoid basic blocking
    headers = {"User-Agent": "Mozilla/5.0"}

    print(f"\nChecking: {url}")

    # Start timer before request
    start = time.time()

    try:
        # Send request to the website
        response = requests.get(url, headers=headers, timeout=10)

        # End timer after response is received
        end = time.time()

        # Calculate total load time
        load_time = end - start

        # Calculate page size in KB
        size_kb = len(response.content) / 1024

        # Print basic metrics
        print(f"Status Code: {response.status_code}")
        print(f"Load Time: {round(load_time, 2)} seconds")
        print(f"Page Size: {round(size_kb, 2)} KB")

        # Approximate time to first byte (server response time)
        print(f"TTFB (approx): {round(response.elapsed.total_seconds(), 2)} seconds")

        # Simple performance rating based on load time
        if load_time < 1:
            print("Speed: FAST")
        elif load_time < 3:
            print("Speed: AVERAGE")
        else:
            print("Speed: SLOW")

    except requests.RequestException as e:
        # Handle connection errors, timeouts, etc.
        print("Error:", e)


if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Check website speed")

    # Accept one or more URLs from the command line
    parser.add_argument("urls", nargs="+", help="List of URLs")

    args = parser.parse_args()

    # Loop through each URL and check its speed
    for url in args.urls:
        check_speed(url)
