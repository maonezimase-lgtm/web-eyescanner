from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def crawler(start_url, max_pages=10):
    print(f"\n--- Crawler: Starting at {start_url} (max {max_pages}) ---")
    visited = set()
    to_visit = [start_url]
    found_links = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue
        try:
            r = requests.get(url, timeout=5)
            visited.add(url)
            soup = BeautifulSoup(r.text, 'lxml')
            for a in soup.find_all('a', href=True):
                link = urljoin(url, a['href'])
                if start_url in link and link not in visited:
                    if link not in to_visit:
                        to_visit.append(link)
                        found_links.append(link)
            print(f"Crawled: {url} | Found {len(found_links)} internal links")
        except:
            continue
    return found_links

