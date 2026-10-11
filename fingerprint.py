import requests


def fingerprint(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        print("\n--- Fingerprint ---")
        print(f"Server: {headers.get('Server', 'Unknown')}")
        print(f"X-Powered-By: {headers.get('X-Powered-By', 'Unknown')}")
        print(f"Content-Type: {headers.get('Content-Type', 'Unknown')}")

        if 'X-Powered-By' in headers:
            print(f"[!] Technology hint: {headers['X-Powered-By']}")

        print("-------------------")
        return headers

    except requests.RequestException as exc:
        print(f"Fingerprint error: {exc}")
        return {}
    except Exception as exc:
        print(f"Unexpected fingerprint error: {exc}")
        return {}
