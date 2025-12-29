# FALCRYS
OSINT Reconnaissance Framework: Python-based tools to collect, analyze, and visualize OSINT data. 

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

---

## Log-Analyser (Planned)

The **Log-Analyser** module is intended to process and extract useful security-relevant information from application and server logs.

The goal of this module is to help identify suspicious patterns, errors, and anomalies that may indicate misconfigurations, attacks, or operational issues.

Planned capabilities include:

* Parsing structured and semi-structured log files
* Identifying failed authentication attempts, unusual request patterns, and error spikes
* Filtering and searching logs based on keywords, IP addresses, timestamps, or status codes
* Producing summarized output to support incident analysis and triage

This module is currently in the design phase and will be implemented as part of the broader FALCRYS reconnaissance and analysis workflow.

---

## Nmap-Automator (Planned)

The **Nmap-Automator** module is designed to automate and standardize common Nmap scanning workflows used during reconnaissance and enumeration.

Instead of manually running multiple Nmap commands, this module aims to orchestrate scans based on target context and collect results in a structured format.

Planned capabilities include:

* Running predefined Nmap scan profiles (basic, service detection, version detection)
* Automating scan selection based on open ports or target type
* Parsing Nmap output for open ports, services, and versions
* Saving scan results in machine-readable formats (JSON/XML)

This module is intended to reduce repetitive manual effort while maintaining control over scan scope and intensity.

---

## Subdomain-Finder (Planned)

The **Subdomain-Finder** module focuses on discovering subdomains associated with a given target domain as part of passive and active reconnaissance.

This module is designed to expand the attack surface map by identifying additional hosts that may expose services, applications, or misconfigurations.

Planned capabilities include:

* Passive subdomain enumeration using public data sources
* Optional active techniques such as DNS brute-forcing
* Deduplication and validation of discovered subdomains
* Output in structured formats for integration with other FALCRYS modules

The module will be implemented with an emphasis on accuracy, rate-limiting, and responsible reconnaissance practices.

