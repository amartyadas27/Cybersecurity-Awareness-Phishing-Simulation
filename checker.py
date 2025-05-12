import re
import requests

def check_url(url):
    # Simple heuristic rules
    suspicious_keywords = ['login', 'verify', 'secure', 'account', 'update']
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return f"⚠️ Suspicious URL (Keyword Found): {url}"

    # Check if URL is reachable
    try:
        response = requests.get(url, timeout=5)
        if response.status_code in [200, 301, 302]:
            return f"✅ Safe-looking URL: {url}"
        else:
            return f"⚠️ URL may be unsafe (status {response.status_code})"
    except Exception as e:
        return f"❌ Could not access URL: {e}"

