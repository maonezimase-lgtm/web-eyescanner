import datetime

def generate_report(url, results, filename="report.txt"):
    print(f"\n--- Generating Report: {filename} ---")
    with open(filename, "w") as f:
        f.write(f"Web Eye Scanner - School Report\n")
        f.write(f"Date: {datetime.datetime.now()}\n")
        f.write(f"Target: {url} (Test site you own)\n")
        f.write(f"="*50 + "\n\n")
        for key, value in results.items():
            f.write(f"{key}:\n{value}\n\n")
        f.write("\nMitigation Tips for Report:\n")
        f.write("- Sanitize all user inputs\n")
        f.write("- Use prepared statements for SQL\n")
        f.write("- Hide Server headers\n")
        f.write("- Only scan with permission\n")
    print(f"Report saved to {filename}")

