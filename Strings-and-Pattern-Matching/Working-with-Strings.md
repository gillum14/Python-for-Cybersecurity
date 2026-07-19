# Working with Strings in Python

## Overview

Strings are one of the most commonly used data types in cybersecurity. Security analysts frequently work with:

- Usernames
- Employee IDs
- Device IDs
- URLs
- IP addresses
- Log files
- Domains
- File paths

This lab introduces common string operations including conversion, concatenation, indexing, slicing, and built-in string methods.

---

# Why It Matters

Nearly every security tool outputs text.

Examples include:

- SIEM logs
- Firewall logs
- DNS records
- URLs
- Hostnames
- Email addresses
- User accounts

Understanding how to manipulate strings makes log analysis and automation significantly easier.

---

# Converting Data Types

Sometimes numeric values need to become strings.

Example

```python
employee_id = 4186

employee_id = str(employee_id)
```

Checking the data type:

```python
print(type(employee_id))
```

Output

```
<class 'str'>
```

---

# Measuring String Length

Use `len()` to count characters.

```python
employee_id = "4186"

print(len(employee_id))
```

Output

```
4
```

---

# Conditional String Validation

Strings can be validated using conditions.

```python
if len(employee_id) < 5:
    print("Employee ID is too short.")
```

Output

```
Employee ID is too short.
```

---

# String Concatenation

The `+` operator joins strings together.

```python
employee_id = "4186"

employee_id = "E" + employee_id
```

Output

```
E4186
```

---

# String Indexing

Each character has an index.

```
r262c36

Index:

0 1 2 3 4 5 6
r 2 6 2 c 3 6
```

Retrieve one character:

```python
device_id[3]
```

Output

```
2
```

---

# String Slicing

Retrieve part of a string.

```python
device_id = "r262c36"

print(device_id[0:3])
```

Output

```
r26
```

Format

```
[start:end]
```

Start is included.

End is excluded.

---

# Working with URLs

Example

```python
url = "https://exampleURL1.com"
```

Extract protocol

```python
print(url[0:8])
```

Output

```
https://
```

---

# Finding Text

Use `.index()` to locate text.

```python
url.index(".com")
```

Output

```
19
```

---

# Saving the Index

```python
ind = url.index(".com")
```

Now the value can be reused.

---

# Extracting the Domain Extension

```python
print(url[ind:ind+4])
```

Output

```
.com
```

---

# Extracting the Website Name

```python
print(url[8:ind])
```

Output

```
exampleURL1
```

---

# Security Applications

String manipulation is commonly used for:

- URL parsing
- Email validation
- Username processing
- Hostname parsing
- IOC extraction
- Log analysis
- Malware filename inspection
- DNS investigations

---

# Lab Summary

During this lab I practiced:

- Converting integers to strings
- Measuring string length
- Validating string data
- Concatenating strings
- Extracting characters
- Using string slicing
- Finding substrings
- Parsing URLs

---

# Key Takeaways

- `str()` converts values into strings.
- `len()` counts characters.
- `+` joins strings together.
- Indexing retrieves one character.
- Slicing extracts part of a string.
- `.index()` locates text inside a string.

---

## Skills Practiced

- Python
- Strings
- String Slicing
- String Indexing
- String Methods
- URL Parsing
- Automation
