import time
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

print("--- NETWORK CHECKER ---")
print("Example: github.com")

website = input("Enter a website: ").strip()

# Uses an example if nothing was entered
if website == "":
    website = "example.com"

# Adds https:// if necessary
if not website.startswith("http://") and not website.startswith("https://"):
    website = "https://" + website

print(f"\nChecking {website} ... ")

start_time = time.perf_counter()

try:
    response = urlopen(website, timeout=5)

    print("Status: Online")
    print("HTTP status code:", response.status)

    response.close()

except HTTPError as error:
    print("Status: Online (the server responded)")
    print("HTTP status code:", error.code)

except URLError as error:
    print("Status: Offline or not reachable")
    print("Error:", error.reason)

except ValueError:
    print("Status: Invalid website address")

response_time = (time.perf_counter() - start_time) * 1000

print("Response time:", round(response_time, 2), "ms")
print("\nCheck finished.")
