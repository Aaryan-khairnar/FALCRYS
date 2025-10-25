import requests
import sys
import json
import re 

def validateinput(website):
    if not website.startswith(('http://', 'https://')):
        website = 'https://' + website
        print(website)
    return website

def single_or_multiple_websites(): 
    choice = input("Single(0) or Multiple(1) websites? [0(default)/1]: ")
    print()
    if choice == '1':
        path = input("Give path of txt file of all urls: ")
        fetch_multiple_head(path)
    else:
        website = validateinput(input("Give website to get headers: "))
        print(json.dumps(fetch_head(website), indent=2))
  

def fetch_head(w):
    try:
        response_header = requests.request('GET', w)
        return dict(response_header.headers)
    except Exception as e:
        print(f"Something went wrong {e}")

def fetch_multiple_head(w):
    output_dict = {}
    output_path = 'output.txt'
    try:
        with open(w, 'r') as url_file: 
            with open(output_path, 'w') as output_file:
                for i, line in enumerate(url_file):
                    print(i,": ", line.strip())
                    output_dict[i]= validateinput(fetch_head(line.strip()))
                    output_file.write(f"{line} : {json.dumps(output_dict[i], indent=2)}\n")
        return output_dict
    except Exception as e:
        print(f"Something is wrong: {e}")

def main():
    single_or_multiple_websites()

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


