# Conditional Statements in Python

## Overview

Conditional statements allow a program to make decisions by executing different code depending on whether a condition evaluates to `True` or `False`.

For cybersecurity professionals, conditionals are used to automate security decisions such as:

- Determining whether systems require updates
- Validating approved users
- Detecting unauthorized access
- Checking login conditions
- Enforcing security policies

---

## Why It Matters

Security automation depends on decision-making.

Instead of manually checking every login or device, Python can automatically evaluate conditions and perform actions based on predefined security rules.

Examples include:

- Blocking unauthorized users
- Alerting on failed logins
- Verifying patch status
- Checking business-hour access
- Enforcing access control policies

---

# Basic if Statement

An `if` statement executes code only when a condition is true.

### Syntax

```python
if condition:
    statement
```

### Example

```python
system = "OS 2"

if system == "OS 2":
    print("No update needed")
```

Output

```
No update needed
```

---

# Comparison Operator

The lab primarily used the equality operator.

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |

Example

```python
system == "OS 2"
```

Returns

```python
True
```

or

```python
False
```

---

# if / else

The `else` block executes whenever the `if` condition evaluates to False.

```python
system = "OS 3"

if system == "OS 2":
    print("No update needed")
else:
    print("Update needed")
```

Output

```
Update needed
```

---

# if / elif / else

Multiple conditions can be checked using `elif`.

```python
if system == "OS 2":
    print("No update needed")
elif system == "OS 1":
    print("Update needed")
elif system == "OS 3":
    print("Update needed")
```

This prevents incorrect messages from appearing for unexpected values.

---

# Logical Operators

Logical operators combine multiple conditions.

## OR

Returns True if either condition is True.

```python
elif system == "OS 1" or system == "OS 3":
    print("Update needed")
```

---

## AND

Returns True only if every condition is True.

```python
if username in approved_list and organization_hours:
    print("Approved login")
```

---

## Membership Operator

The `in` operator checks whether a value exists inside a list.

Example

```python
approved_list = [
    "elarson",
    "bmoreno",
    "tshah"
]

username = "bmoreno"

if username in approved_list:
    print("Access granted")
```

Output

```
Access granted
```

---

# Boolean Values

Many conditions evaluate to Boolean values.

```python
True
False
```

Example

```python
organization_hours = True
```

```python
if organization_hours:
    print("Login during organization hours.")
```

---

# Login Authorization Example

```python
approved_list = [
    "elarson",
    "bmoreno",
    "tshah",
    "sgilmore",
    "eraab"
]

username = "jhill"

if username in approved_list:
    print("This user has access.")
else:
    print("Access denied.")
```

---

# Combining Multiple Conditions

```python
approved_list = [
    "elarson",
    "bmoreno",
    "tshah",
    "sgilmore",
    "eraab"
]

username = "bmoreno"

organization_hours = True

if username in approved_list and organization_hours:
    print("Approved login during organization hours.")
else:
    print("Login denied.")
```

---

# Security Applications

Conditional statements are commonly used to:

- Verify user authorization
- Check login times
- Detect failed authentication attempts
- Validate MFA status
- Trigger alerts
- Block malicious activity
- Verify operating system versions
- Enforce password policies

---

# Lab Summary

During this lab I practiced:

- if statements
- else statements
- elif statements
- comparison operators
- Boolean values
- logical operators
- membership testing with `in`
- writing authentication logic

---

# Key Takeaways

- `if` executes code when a condition is True.
- `else` handles every remaining case.
- `elif` allows multiple conditions to be checked.
- `==` compares values.
- `and` requires every condition to be True.
- `or` requires only one condition to be True.
- `in` checks whether an item exists in a collection.
- Conditional statements form the foundation of security automation.

---

## Skills Practiced

- Python
- Conditional Statements
- Boolean Logic
- Authentication
- Authorization
- Access Control
- Security Automation
