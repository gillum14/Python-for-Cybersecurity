import re

log_data = """
192.168.152.148
192.168.22.115
192.168.190.178
192.168.96.200
192.168.174.117
192.168.168.144
"""

pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

valid_ips = re.findall(pattern, log_data)

flagged = {
    "192.168.190.178",
    "192.168.96.200",
    "192.168.174.117",
    "192.168.168.144"
}

for ip in valid_ips:
    if ip in flagged:
        print(f"[!] {ip} requires investigation")
    else:
        print(f"[+] {ip} appears normal")
