"""Report organic web sessions and App Store handoffs by landing page."""
import argparse
import csv
from datetime import date
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def exact(field, value):
    return {"filter": {"fieldName": field, "stringFilter": {"matchType": "EXACT", "value": value}}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("start", type=date.fromisoformat)
    parser.add_argument("end", type=date.fromisoformat)
    args = parser.parse_args()
    if args.end < args.start:
        parser.error("end precedes start")
    token = os.environ.get("GA4_ACCESS_TOKEN")
    if not token:
        parser.error("Set GA4_ACCESS_TOKEN to a read-only Analytics OAuth access token")
    config = json.loads((Path(__file__).resolve().parents[1] / "site/analytics.json").read_text())
    endpoint = f"https://analyticsdata.googleapis.com/v1beta/properties/{config['property_id']}:runReport"
    payload = {
        "dateRanges": [{"startDate": str(args.start), "endDate": str(args.end)}],
        "dimensions": [{"name": "landingPage"}, {"name": "eventName"}],
        "metrics": [{"name": "sessions"}, {"name": "eventCount"}],
        "dimensionFilter": {"andGroup": {"expressions": [
            exact("streamId", config["stream_id"]),
            exact("sessionDefaultChannelGroup", "Organic Search"),
            {"orGroup": {"expressions": [exact("eventName", e) for e in ("page_view", "app_store_click")]}}
        ]}},
        "limit": 250000
    }
    req = Request(endpoint, data=json.dumps(payload).encode(), headers={
        "Authorization": f"Bearer {token}", "Content-Type": "application/json"
    })
    try:
        with urlopen(req, timeout=45) as response:
            result = json.load(response)
    except HTTPError as error:
        sys.exit(f"GA4 HTTP {error.code}: {error.read().decode()}")
    rows = {}
    for row in result.get("rows", []):
        landing, event = (item["value"] for item in row["dimensionValues"])
        sessions, count = (int(item["value"]) for item in row["metricValues"])
        counts = rows.setdefault(landing, {})
        counts[event] = (sessions, count)
    writer = csv.writer(sys.stdout)
    writer.writerow(["landing_page", "organic_sessions_with_page_view", "organic_page_views",
                     "organic_sessions_with_store_click", "organic_store_clicks"])
    for landing, counts in sorted(rows.items()):
        writer.writerow([landing, *counts.get("page_view", (0, 0)), *counts.get("app_store_click", (0, 0))])
    if not rows:
        print("No reportable matching rows.", file=sys.stderr)


if __name__ == "__main__":
    main()
