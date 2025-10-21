import requests

def single_or_multiple_websites() -> str: 
    choice = int(input("Single(0) or Multiple(1) websites? [0/1]:"))
    if (choice == 0):
        w = input("Give website to get json errors: ")
    else:
        pass
    return w
    

def fetch_head(w): 
    response_header = requests.request('GET', w)
    return response_header.headers

def main():
    website = single_or_multiple_websites()
    header = fetch_head(website)
    print(header)

if __name__ == '__main__':
    main()

'''
Server — server/banner (Apache, nginx, Cloudflare, etc.). Good for fingerprinting.
X-Powered-By — framework or language (PHP, Express, etc.).
Content-Type — resource type (is it HTML, JSON, etc.).
Set-Cookie — insecure cookie flags (Missing HttpOnly/Secure).
Strict-Transport-Security (HSTS) — HTTPS enforcement.
Content-Security-Policy (CSP) — presence/absence and misconfigurations.
X-Frame-Options — clickjacking protection.
X-Content-Type-Options — sniffing protection.
Referrer-Policy, Permissions-Policy / Feature-Policy — privacy/feature constraints.
Location — redirect targets (open-redirect hunting).
Cache-Control, ETag — caching characteristics.
Via, X-Forwarded-For, Forwarded — presence of proxies/load balancers.
Retry-After — rate-limit hint.
Expect-CT, X-XSS-Protection (deprecated but informative).
Content-Length, Allow — methods allowed (if Allow present).
'''


