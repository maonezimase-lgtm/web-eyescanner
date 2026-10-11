import requests

def dir_enum(base_url, wordlist_path="wordlists/common_dirs.txt"):
    print(f"\n--- Dir Enum: Checking {base_url} ---")
    found = []
    try:
        with open(wordlist_path, "r") as f:
            for line in f:
                path = line.strip()
                if not path:
                    continue
                test_url = base_url.rstrip("/") + path
                try:
                    r = requests.get(test_url, timeout=3)
                    if r.status_code == 200:
                        print(f"FOUND: {test_url} [{r.status_code}]")
                        found.append(test_url)
                except:
                    continue
    except FileNotFoundError:
        print(f"Wordlist not found: {wordlist_path}")
    return found
