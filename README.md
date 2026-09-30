# 🔐 Network Port Scanner

A Python-based network port scanner that detects open ports and identifies running services on a target host.

## Features
- Resolves hostname to IP address
- Scans a custom port range
- Identifies common services (SSH, HTTP, FTP, RDP, etc.)
- Clean formatted output with timestamps

## Usage
```bash
python scanner.py
```

## Example Output
Target : scanme.nmap.org
Resolved IP: 45.33.32.156

[OPEN] Port 22 → SSH
[OPEN] Port 80 → HTTP

Scan complete — 2 open port(s) found

## Technologies
- Python
- Socket Programming
- Network Security Concepts

## Disclaimer
Only scan hosts you have permission to scan.
