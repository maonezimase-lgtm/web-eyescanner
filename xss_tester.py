import requests
from urllib.parse import urljoin
try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

def xss_tester(url):
    print("\n--- [XSS Tester] ---")
    if not BeautifulSoup:
        print("BeautifulSoup not installed, skipping")
        return False
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent":"Mozilla/5.0"})
        soup = BeautifulSoup(r.text, 'lxml')
        forms = soup.find_all('form')
        if not forms:
            print("No forms found - No XSS form to test (Safe)")
            return False
        print(f"Found {len(forms)} form(s)")
        for form in forms:
            action = form.get('action')
            target = urljoin(url, action) if action else url
            print(f"  Form action -> {target}")
        return False
    except Exception as e:
        print(f"XSS error: {e}")
        return False
