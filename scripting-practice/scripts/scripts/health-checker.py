
import urllib.request
import urllib.error
import time 

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.amazon.com"
]

print("SERVER HEALTH CHECK")
print("-------------------")

for URL in websites:

    print(f"\nChecking: {URL}")
    start_time = time.time()

    try:
        response = urllib.request.urlopen(URL, timeout=10)
        end_time = time.time()
        response_time = end_time - start_time
        print(f"Response Time: {response_time:.2f} seconds")

        status_code = response.status

        if 200 <= status_code < 300:
            print("STATUS: HEALTHY")
            print(f"HTTP Status Code: {status_code}")
        else:
            print("ALERT: Server returned an unsuccessful status code.")
            print(f"HTTP Status Code: {status_code}")

    except urllib.error.HTTPError as error:
        print("ALERT: Server returned an HTTP error.")
        print(f"HTTP Status Code: {error.code}")

    except urllib.error.URLError as error:
        print("ALERT: Unable to reach the server.")
        print(f"Reason: {error.reason}")

    except TimeoutError:
        print("ALERT: Server request timed out.")
