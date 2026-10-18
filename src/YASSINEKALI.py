#!/usr/bin/env python3
"""
ip_tracker.py — Educational IP geolocation tool.
"""

import sys
import ipaddress
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

APIS = [
    "http://ip-api.com/json/{ip}?fields=status,country,regionName,"
    "city,isp,org,as,query,timezone,lat,lon",
    "https://ipwho.is/{ip}",
    "https://ipinfo.io/{ip}/json",
]

def validate(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
    except ValueError:
        return None, "invalid IP format"
    if ip.is_private:
        return None, "private range — not routable"
    if ip.is_loopback:
        return None, "loopback address"
    if ip.is_multicast:
        return None, "multicast address"
    return ip, None

def query_all(ip_str):
    merged = {}
    for tpl in APIS:
        try:
            r = requests.get(tpl.format(ip=ip_str), timeout=8, verify=False)
            data = r.json()
            if isinstance(data, dict) and data.get("status") != "fail":
                merged.update(data)
        except Exception:
            continue
    return merged

def print_report(d):
    ip      = d.get("query") or d.get("ip", "?")
    city    = d.get("city", "?")
    region  = d.get("regionName") or d.get("region", "?")
    country = d.get("country") or d.get("country_name", "?")
    isp     = d.get("isp") or d.get("connection", {}).get("isp") \
              or d.get("org", "?")
    tz      = d.get("timezone", "?")
    lat     = d.get("lat") or d.get("latitude")
    lon     = d.get("lon") or d.get("longitude")

    print("=" * 40)
    print("IP INFORMATION")
    print("=" * 40)
    print(f"IP       : {ip}")
    print(f"City     : {city}")
    print(f"Region   : {region}")
    print(f"Country  : {country}")
    print(f"ISP      : {isp}")
    print(f"Timezone : {tz}")

    if lat and lon:
        print()
        print("Map links:")
        print(f"  Google : https://www.google.com/maps?q={lat},{lon}")
        print(f"  OSM    : https://www.openstreetmap.org/?mlat={lat}&mlon={lon}")

def main():
    if len(sys.argv) != 2:
        print("usage: python ip_tracker.py <ip>")
        sys.exit(1)
    ip, err = validate(sys.argv[1])
    if err:
        print(f"error: {err}")
        sys.exit(1)
    data = query_all(str(ip))
    if not data:
        print("error: no API returned data")
        sys.exit(1)
    print_report(data)

if __name__ == "__main__":
    main()
