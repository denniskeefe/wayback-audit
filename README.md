# Wayback Machine Domain Auditor

**Note: This was vibe coded with Gemini**

This script queries the Wayback Machine's CDX API to find archived snapshots of a specific domain within a user-defined date range. It filters for successful captures (HTTP 200) and exports the results to a CSV file for auditing and analysis.

---

## Features

* **Custom Date Filtering**: Specify a start date and an optional end date for the audit.
* **Status Filtering**: Automatically filters for successful `200 OK` status codes.
* **Deduplication**: Uses the Wayback Machine's collapse parameter to ensure unique daily captures.
* **CSV Export**: Generates a structured report including:
* Formatted capture date (YYYY-MM-DD HH:MM)
* HTTP Status Code
* Original URL
* Direct link to the Wayback Machine archive



---

## Prerequisites

* Python 3.x
* `requests` library

To install the required library, run:

```bash
pip install requests

```

---

## Usage

1. **Run the script**:
```bash
python script_name.py

```


2. **Enter the Domain**: Input the domain you wish to audit (e.g., `example.com`).
3. **Enter the Start Date**: Provide the date in `YYYYMMDD` format (e.g., `20240101`).
4. **Enter the End Date**: Provide the end date in `YYYYMMDD` format, or press **Enter** to default to the current date.

---

## How it Works

The script interacts with the Internet Archive's CDX API. Below is a high-level overview of the data flow:

1. **Request**: The script sends a GET request to `web.archive.org/cdx/search/cdx`.
2. **Parameters**: It applies filters for the `url`, `statuscode`, and `timestamp`.
3. **Processing**: The script converts the raw API timestamp (e.g., `20240101123000`) into a human-readable format.
4. **Output**: Data is written row-by-row into a CSV file named `audit_[domain]_[start_date].csv`.

---

## Data Structure

The generated CSV follows this format:

| Date | Status | Original URL | View Archive Link |
| --- | --- | --- | --- |
| 2024-01-01 12:00 | 200 | [http://example.com/](https://www.google.com/search?q=http://example.com/) | [https://web.archive.org/web/20240101120000/http://example.com/](https://www.google.com/search?q=https://web.archive.org/web/20240101120000/http://example.com/) |

---

