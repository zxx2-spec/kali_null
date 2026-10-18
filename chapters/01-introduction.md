# Chapter 1 — Introduction

Every device on the internet has an IP address. It is not a name, not a person, not a location — it is a routing label. This book is about reading that label. We will build a small Python tool that reads public IP metadata through three APIs, merges the result, and prints a clean report.

## What we build

- `src/YASSINEKALI.py` — a single-file Python script
- Three public APIs (ip-api, ipwho, ipinfo)
- No authentication, no private IPs, no tracking of people

## Requirements

- Python 3.8+
- `pip install requests`
