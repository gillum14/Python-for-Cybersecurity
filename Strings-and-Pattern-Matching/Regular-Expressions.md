# Use Regular Expressions to Find Patterns

## Overview

Regular expressions (Regex) are pattern-matching tools used to search, extract, and validate text.

Security analysts frequently use regex to automate:

- Log analysis
- IOC detection
- IP address extraction
- Email validation
- Device identification
- Threat hunting

Python provides regex functionality through the built-in `re` module.

---

# Why It Matters

Security teams process thousands (or millions) of log entries.

Instead of manually reading every line, regex can automatically locate:

- IP addresses
- Device IDs
- Domains
- URLs
- Hashes
- Email addresses
- Usernames
- Suspicious strings

Regex is commonly used in:

- SIEM searches
- IDS/IPS rules
- Log parsing
- Malware analysis
- DFIR investigations

---

# Importing Regex

```python
import re
```

The `re` module provides functions for searching and matching text.

---

# Finding Device IDs

Example log:

```
r262c36
67bv8fy
r151dm4
r15xk9h
```

Regex pattern:

```python
r15\w+
```

Explanation:

| Pattern | Meaning |
|----------|---------|
| r15 | Starts with r15 |
| \w | Any letter, number, or underscore |
| + | One or more characters |

---

# Searching with findall()

```python
re.findall(pattern, devices)
```

Returns:

```python
[
'r151dm4',
'r15xk9h',
'r15u9q5',
'r159r1u'
]
```

---

# Matching IP Addresses

Initial pattern:

```python
\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d
```

Matches:

```
192.168.152.148
```

Problem:

Does NOT match

```
192.168.22.115
```

because every section isn't exactly three digits.

---

# Flexible Matching

Improved pattern:

```python
\d+\.\d+\.\d+\.\d+
```

Now matches:

```
192.168.22.115
```

Problem:

It also matches invalid addresses like:

```
19245.168.2345.49
```

---

# Limiting Digits

Best pattern from this lab:

```python
\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
```

Meaning:

```
1–3 digits
.
1–3 digits
.
1–3 digits
.
1–3 digits
```

This extracts valid IPv4 formatting.

---

# Comparing Against Flagged Addresses

Example:

```python
flagged_addresses = [
    "192.168.190.178",
    "192.168.96.200"
]
```

Loop:

```python
for address in valid_ip_addresses:

    if address in flagged_addresses:
        print("Flagged")

    else:
        print("Safe")
```

---

# Regex Symbols Learned

| Symbol | Meaning |
|---------|---------|
| \w | Letter, number, underscore |
| \d | Digit |
| . | Literal period (escaped as \.) |
| + | One or more |
| {1,3} | Between 1 and 3 occurrences |

---

# Useful Regex Functions

| Function | Purpose |
|----------|---------|
| re.findall() | Return all matches |
| re.search() | Find first match |
| re.match() | Match from beginning |
| re.sub() | Replace text |
| re.split() | Split text |

---

# Security Applications

Regex is commonly used for:

- SIEM detections
- IOC extraction
- Threat hunting
- Email filtering
- Log parsing
- Firewall rule validation
- Malware detection
- YARA rule development

---

# Skills Practiced

- Importing modules
- Regular expressions
- Pattern matching
- Log parsing
- Lists
- Loops
- Conditionals
- Membership testing

---

# Key Takeaways

- Regex automates searching large datasets.
- `re.findall()` extracts every match.
- Regex patterns become more precise using quantifiers.
- Python can automatically identify suspicious IP addresses from log files.
