#!/usr/bin/env python3
"""Fetch live arrivals for Montreal-Trudeau (YUL) from Flightradar24's public API.

Usage:
    python3 scripts/fetch_yul_arrivals.py > data/yul_arrivals_$(date +%F).json

Outputs a JSON document with airport metadata and one record per arrival:
flight number, callsign, airline, origin, scheduled/estimated/actual arrival
times (UTC), status, aircraft type, and registration.
"""
import json
import time
import urllib.request

AIRPORT = "yul"
PAGES = (1, 2)  # 100 flights per page — 2 pages covers roughly a day


def iso(ts):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts)) if ts else None


def fetch_arrivals():
    now = int(time.time())
    rows = []
    for page in PAGES:
        url = (
            f"https://api.flightradar24.com/common/v1/airport.json?code={AIRPORT}"
            "&plugin[]=schedule&plugin-setting[schedule][mode]=arrivals"
            f"&plugin-setting[schedule][timestamp]={now}&page={page}&limit=100"
        )
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
            "Accept": "application/json",
        })
        payload = json.load(urllib.request.urlopen(req, timeout=30))
        sched = payload["result"]["response"]["airport"]["pluginData"]["schedule"]["arrivals"]
        for item in sched["data"]:
            f = item["flight"]
            t = f.get("time", {})
            origin = f.get("airport", {}).get("origin") or {}
            rows.append({
                "flight": (f.get("identification", {}).get("number", {}) or {}).get("default"),
                "callsign": f.get("identification", {}).get("callsign"),
                "airline": (f.get("airline") or {}).get("name"),
                "origin_airport": origin.get("name"),
                "origin_iata": (origin.get("code") or {}).get("iata"),
                "scheduled_arrival_utc": iso((t.get("scheduled") or {}).get("arrival")),
                "estimated_arrival_utc": iso((t.get("estimated") or {}).get("arrival")),
                "actual_arrival_utc": iso((t.get("real") or {}).get("arrival")),
                "status": (f.get("status", {}) or {}).get("text"),
                "aircraft": ((f.get("aircraft") or {}).get("model") or {}).get("text") or None,
                "registration": (f.get("aircraft") or {}).get("registration") or None,
            })
        if page >= sched.get("page", {}).get("total", 1):
            break
    return {
        "source": "flightradar24.com",
        "meta": {
            "airport": "Montreal-Pierre Elliott Trudeau International Airport",
            "iata": "YUL",
            "icao": "CYUL",
            "timezone": "America/Toronto",
            "fetched_utc": iso(now),
        },
        "count": len(rows),
        "arrivals": rows,
    }


if __name__ == "__main__":
    print(json.dumps(fetch_arrivals(), ensure_ascii=False, indent=2))
