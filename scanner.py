#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from fingerprint import fingerprint
from crawler import crawler
from dir_enum import dir_enum
from xss_tester import xss_tester
from sqli_tester import sqli_tester
from reporting import generate_report

url = input("Enter URL to scan (use your own test site): ").strip()
if not url.startswith("http"):
    url = "https://" + url

results = {}

try:
    print(f"\n[1] Scanning {url}...")
    r = requests.get(url, timeout=5)
    print(f"Status: {r.status_code}")
    results["Status"] = r.status_code

    print(f"\n[2] Fingerprint")
    headers = fingerprint(url)
    results["Headers"] = str(headers)

    soup = BeautifulSoup(r.text, 'lxml')
    title = soup.title.string if soup.title else 'No title'
    print(f"\n[3] Page Title: {title}")
    results["Title"] = title

    print(f"\n[4] Dir Enum")
    found_dirs = dir_enum(url)
    results["Directories Found"] = str(found_dirs)

    print(f"\n[5] Crawler")
    links = crawler(url, max_pages=5)
    results["Crawled Links"] = str(links[:10])

    print(f"\n[6] XSS Check")
    xss_tester(url)

    print(f"\n[7] SQLi Check")
    sqli_tester(url)

    generate_report(url, results)
    print("\nDone! Check report.txt for your school submission.")

except Exception as e:
    print(f"Error: {e}")
    print("Tip: Make sure you type full URL like https://example.com")

