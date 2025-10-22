import requests
import os
# import json

def single_or_multiple_websites(): 
    choice = '0'
    choice = input("Single(0) or Multiple(1) websites? [0(default)/1]: ")
    print()
    if choice == '0':
        website = input("Give website to get headers: ")
        print(fetch_head(website))
    else:
        path = input("Give path of txt file of all urls: ")
        fetch_multiple_head(path)
    

def fetch_head(w): 
    response_header = requests.request('GET', w)
    return response_header.headers

def fetch_multiple_head(w):
    output_dict = {}
    output_path = 'output.txt'
    try:
        with open(w, 'r') as url_file: 
            with open(output_path, 'w') as output_file:
                for i, line in enumerate(url_file):
                    print(i,": ", line.strip())
                    output_dict[i]= fetch_head(line.strip())
#                    output_file.write(f"{i}:{json.dumps(fetch_head(line.strip()), indent=2)}\n")
                    output_file.write(f"{i}: {fetch_head(line.strip())}\n")

        return output_dict
    except Exception as e:
        print(f"Something is wrong: {e}")

def main():
    website = single_or_multiple_websites()
    

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


