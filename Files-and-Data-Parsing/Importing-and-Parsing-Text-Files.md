# Import and Parse Text Files

## Overview

Security analysts frequently work with log files stored as plain text.

Python provides built-in tools for:

- Reading files
- Writing files
- Appending data
- Parsing text
- Converting text into lists for analysis

These skills are foundational for log analysis, automation, and incident response.

---

# Why It Matters

Nearly every cybersecurity tool exports data to text files:

- Authentication logs
- Firewall logs
- Web server logs
- IDS alerts
- IOC lists
- Allow/Deny lists

Python makes these files easy to process automatically.

---

# Opening Files

The safest way to open files is with a `with` statement.

```python
with open("login.txt", "r") as file:
```

The `with` statement automatically closes the file when finished.

---

# File Modes

| Mode | Purpose |
|------|---------|
| `"r"` | Read |
| `"w"` | Write (overwrite) |
| `"a"` | Append |
| `"x"` | Create new file |

---

# Reading Files

Read an entire file:

```python
with open("login.txt", "r") as file:
    text = file.read()

print(text)
```

Returns the entire contents as one string.

---

# Splitting Text

Convert one large string into a list.

```python
text.split()
```

Example:

Before:

```
one long string
```

After:

```python
[
"line1",
"line2",
"line3"
]
```

---

# Appending Data

Append new information without deleting existing data.

```python
with open("login.txt", "a") as file:
    file.write(new_entry)
```

Useful for:

- New log entries
- Audit records
- Incident tracking

---

# Writing Files

Create or overwrite a file.

```python
with open("allow_list.txt", "w") as file:
    file.write(ip_addresses)
```

Use carefully.

`"w"` replaces everything already in the file.

---

# Reading Newly Written Files

```python
with open("allow_list.txt", "r") as file:
    text = file.read()

print(text)
```

---

# Common File Methods

| Method | Purpose |
|---------|----------|
| open() | Opens a file |
| read() | Reads entire file |
| write() | Writes text |
| split() | Converts string to list |
| close() | Closes file (automatic with `with`) |

---

# Security Applications

Python file handling is commonly used for:

- Importing authentication logs
- Reading firewall logs
- Parsing IDS alerts
- Reading IOC lists
- Creating allow lists
- Exporting investigation results
- Updating incident reports

---

# Skills Practiced

- File handling
- Reading files
- Writing files
- Appending data
- Parsing text
- String manipulation

---

# Key Takeaways

- Use `with open()` to safely work with files.
- `"r"` opens files for reading.
- `"w"` creates or overwrites files.
- `"a"` appends data to existing files.
- `.read()` imports an entire file as a string.
- `.split()` converts text into a list for easier analysis.
