# FALCRYS
OSINT Reconnaissance Tool: Developed a Python-based tool to collect, analyze, and visualize OSINT data. 

## 1. Header-Fetch (Implemented)

The **Header-Fetch** module is the first implemented component of FALCRYS.
It focuses on **passive HTTP reconnaissance** by fetching response headers from one or multiple web targets.

This module is designed to provide raw header data that can later be analyzed for fingerprinting, security posture assessment, and reconnaissance workflows.

### What it does

* Sends HTTP requests to a target URL (or multiple URLs from a file)
* Retrieves and outputs the full set of HTTP response headers
* Supports both:
  - Single target input
  - Multiple targets via a text file (one URL per line)
* Handles basic input validation by normalizing URLs (`http://` / `https://`)
* Allows configurable request timeout

At this stage, the module **only fetches and outputs headers**.
Automated analysis and classification of headers will be added in later iterations.

### Headers collected (if present)

The tool fetches all response headers returned by the server. Commonly useful headers include:

* `Server` — server/banner information (Apache, nginx, Cloudflare, etc.)
* `X-Powered-By` — backend framework or language hints
* `Content-Type` — response content type
* `Set-Cookie` — cookie attributes and flags
* `Strict-Transport-Security` (HSTS)
* `Content-Security-Policy` (CSP)
* `X-Frame-Options`
* `X-Content-Type-Options`
* `Referrer-Policy`
* `Permissions-Policy` / `Feature-Policy`
* `Location` — redirect targets
* `Cache-Control`, `ETag`
* `Via`, `X-Forwarded-For`, `Forwarded`
* `Retry-After`
* `Expect-CT`, `X-XSS-Protection`
* `Content-Length`, `Allow`

The presence or absence of these headers can later be used for security insight and fingerprinting.

### Usage

Single target:

```
python header_fetch.py --url example.com
```

Multiple targets from file:

```
python header_fetch.py --path urls.txt
```

Optional timeout (in seconds):

```
python header_fetch.py --url example.com --t 5
```

If no command-line arguments are provided, the script falls back to an interactive mode allowing the user to choose between single or multiple targets.

### Output

* For a single target, headers are printed to standard output in JSON format.
* For multiple targets, headers are written to `output.txt` with each target’s headers serialized as JSON.

### Current limitations

* No automated analysis or scoring of headers yet
* No concurrency or async requests
* No TLS certificate inspection
* No rate limiting or retry logic

These features are planned as future enhancements.

### Planned improvements

* Header analysis and security posture checks
* Async or threaded fetching for large target lists
* TLS certificate inspection (expiry, issuer, SANs)
* Structured JSON/CSV output
* Modular integration with other FALCRYS recon components

## 2. Log-Parser

## 3. Nmap-Automator

## 4. Subdomain-Finder
