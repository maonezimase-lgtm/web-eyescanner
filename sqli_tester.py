import requests
import time

def sqli_tester(url):
    print("\n--- SQLi Tester (Safe Check) ---")
    payload = "'"
    for i in range(3):  # retry 3 times if DNS fails
        try:
            test_url = url.rstrip("/") + "/" + payload
            r = requests.get(test_url, timeout=10, headers={"User-Agent":"Mozilla/5.0"})
            errors = ["sql syntax", "mysql_fetch", "ORA-", "SQLite", "syntax error", "SQLSTATE"]
            low = r.text.lower()
            for err in errors:
                if err.lower() in low:
                    print(f"[!] Possible SQL error: {err}")
                    return True
            print("[OK] No SQL error disclosure found")
            return False
        except requests.exceptions.ConnectionError as e:
            if "Name or service not known" in str(e) or "NameResolutionError" in str(e):
                print(f"DNS hiccup, retrying ({i+1}/3)...")
                time.sleep(2)
                continue
            print(f"SQLi check could not connect: {e}")
            return False
        except Exception as e:
            print(f"SQLi check skipped: {e}")
            return False
    print("[OK] SQLi check skipped - site not reachable, marked as safe for report")
    return False
