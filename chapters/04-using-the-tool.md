# Chapter 4 — Using the tool

## Basic usage

```bash
python src/YASSINEKALI.py 8.8.8.8
```

Output example:

```
========================================
IP INFORMATION
========================================
IP       : 8.8.8.8
City     : Mountain View
Region   : California
Country  : United States
ISP      : Google LLC
Timezone : America/Los_Angeles

Map links:
  Google : https://www.google.com/maps?q=37.4056,-122.0775
  OSM    : https://www.openstreetmap.org/?mlat=37.4056&mlon=-122.0775
```

## Private IPs

The tool rejects private IPs early because they cannot be geolocated.

```bash
python src/YASSINEKALI.py 192.168.1.1
# error: private range — not routable
```

## Notes on accuracy

- **Country** is highly reliable (registry-backed).
- **City** is often the ISP's routing hub, not the user's home.
- **Lat/Lon** is the city centroid — not a house, not a person.
- **VPNs** and proxies will show the VPN's location, not the user's.
