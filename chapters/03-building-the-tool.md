# Chapter 3 — Building the tool

Full source: `src/YASSINEKALI.py`.

## Step 1 — Validate the IP

```python
import ipaddress

def validate(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
    except ValueError:
        return None, "invalid format"
    if ip.is_private:
        return None, "private range"
    return ip, None
