import re

log_data = """
User login from 192.168.152.148
Failed login from 192.168.22.115
Alert from 1923.1689.3.24
Another login 192.168.174.117
"""

pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

ips = re.findall(pattern, log_data)

print(ips)
