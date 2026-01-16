import requests
import csv
from datetime import datetime

def run_dated_audit():
    domain = input("Enter domain (e.g., example.com): ").strip()
    start_date = input("Start Date (YYYYMMDD, e.g., 20240101): ").strip()
    end_date = input("End Date (YYYYMMDD, or press Enter for today): ").strip()

    params = {
        "url": f"{domain}/*",
        "output": "json",
        "fl": "timestamp,original,statuscode",
        "filter": "statuscode:200",
        "from": start_date,
        "collapse": "timestamp:10"
    }
    
    if end_date:
        params["to"] = end_date

    try:
        print(f"Checking captures from {start_date} onwards...")
        response = requests.get("http://web.archive.org/cdx/search/cdx", params=params)
        response.raise_for_status()
        
        data = response.json()
        if len(data) <= 1:
            print("No captures found in this date range.")
            return

        filename = f"audit_{domain}_{start_date}.csv"
        
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Status", "Original URL", "View Archive Link"])
            
            for entry in data[1:]:
                ts, original_url, status = entry
                readable_date = datetime.strptime(ts, '%Y%m%d%H%M%S').strftime('%Y-%m-%d %H:%M')
                archive_link = f"https://web.archive.org/web/{ts}/{original_url}"
                writer.writerow([readable_date, status, original_url, archive_link])
        
        print(f"Saved {len(data)-1} entries to {filename}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_dated_audit()
