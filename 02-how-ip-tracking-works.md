# Chapter 2 — How IP tracking works

## The three layers

1. **The IP itself** — IPv4 or IPv6. Public or private.
   Private ranges are not routable on the internet.

2. **The registry** — IANA → RIR → ISP. Who owns the block.

3. **The geolocation database** — MaxMind, ipinfo, ip-api
   map blocks to cities. Country accurate ~99%, city ~50-80%.

## What APIs return

| Field     | Reliability | Notes                       |
|-----------|-------------|-----------------------------|
| Country   | High        | Registry-backed             |
| Region    | Medium      | Database-backed             |
| City      | Medium-Low  | Often the ISP's hub         |
| ISP / ASN | High        | Registry-backed             |
| Lat / Lon | Low         | City centroid, not a person |

## The three APIs

- `ip-api.com` — free, no key, 45 req/min
- `ipwho.is` — free, generous limits
- `ipinfo.io` — free tier, basic fields

We query all three and merge. Redundancy beats single source.
