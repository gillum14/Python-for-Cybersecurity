# Variables and Data Types

## Overview

Variables allow Python programs to store and manage information. In cybersecurity, variables can represent usernames, device identifiers, login attempts, authentication status, IP addresses, security alerts, and other data used during investigations or automation.

This exercise demonstrates how to assign values to variables, determine their data types, update stored values, and compare numeric values.

---

## Why It Matters

Security analysts may use variables to track:

- Approved users
- Device identifiers
- Login attempts
- Account status
- Security alert counts
- Authentication results
- File paths
- Network addresses

Understanding variables and data types is essential before building more advanced security scripts.

---

## Assignment Operator

The assignment operator (`=`) stores a value in a variable.

```python
device_id = "72e08x0"
```

In this example:

- `device_id` is the variable name.
- `=` assigns the value.
- `"72e08x0"` is the stored string.

---

## Strings

Strings store text and are written inside quotation marks.

```python
device_id = "72e08x0"
```

Display the value:

```python
print(device_id)
```

Output:

```text
72e08x0
```

Check the data type:

```python
device_id_type = type(device_id)
print(device_id_type)
```

Output:

```text
<class 'str'>
```

The `str` data type represents a string.

---

## Lists

Lists store multiple values in a single variable.

```python
username_list = [
    "madebowa",
    "jnguyen",
    "tbecker",
    "nhersh",
    "redwards"
]
```

Display the list:

```python
print(username_list)
```

Check the data type:

```python
username_list_type = type(username_list)
print(username_list_type)
```

Output:

```text
<class 'list'>
```

---

## Reassigning Variables

Variables can be updated by assigning them a new value.

```python
username_list = [
    "madebowa",
    "jnguyen",
    "tbecker",
    "nhersh",
    "redwards"
]

print(username_list)
```

Updated list:

```python
username_list = [
    "madebowa",
    "jnguyen",
    "tbecker",
    "nhersh",
    "redwards",
    "lpope"
]

print(username_list)
```

The second assignment replaces the previous value stored in `username_list`.

> In a real program, adding a single user with `append()` would usually be cleaner than rewriting the entire list.

```python
username_list.append("lpope")
```

---

## Integers

Integers store whole numbers.

```python
max_logins = 3
login_attempts = 2
```

Check their data types:

```python
print(type(max_logins))
print(type(login_attempts))
```

Output:

```text
<class 'int'>
<class 'int'>
```

The `int` data type represents an integer.

---

## Comparison Operators

Comparison operators compare values and return a Boolean result.

```python
login_attempts <= max_logins
```

The `<=` operator means **less than or equal to**.

### Allowed Number of Attempts

```python
max_logins = 3
login_attempts = 2

print(login_attempts <= max_logins)
```

Output:

```text
True
```

The user has not exceeded the maximum number of login attempts.

### Exceeded Number of Attempts

```python
max_logins = 3
login_attempts = 4

print(login_attempts <= max_logins)
```

Output:

```text
False
```

The user has exceeded the maximum number of login attempts.

---

## Boolean Values

Boolean values represent one of two states:

- `True`
- `False`

Example:

```python
login_status = False
```

Check the data type:

```python
login_status_type = type(login_status)
print(login_status_type)
```

Output:

```text
<class 'bool'>
```

Booleans are commonly used to represent:

- Whether a login succeeded
- Whether an account is active
- Whether a device is compliant
- Whether an alert requires action
- Whether access should be granted

---

## Data Types Practiced

| Data Type | Description | Example |
|---|---|---|
| `str` | Text | `"72e08x0"` |
| `list` | Collection of values | `["user1", "user2"]` |
| `int` | Whole number | `3` |
| `bool` | True or false value | `False` |

---

## Functions Practiced

### `print()`

Displays information.

```python
print(device_id)
```

### `type()`

Returns the data type of an object.

```python
print(type(device_id))
```

---

## Practical Cybersecurity Uses

Variables and data types can support:

- Login monitoring
- Allow-list management
- Account lockout logic
- Security alert tracking
- Authentication workflows
- Device inventory management
- Automated security checks

---

## Lab Summary

During this lab, I practiced:

- Assigning values to variables
- Working with strings
- Creating lists
- Updating variable values
- Working with integers
- Comparing numeric values
- Working with Boolean values
- Identifying data types with `type()`
- Displaying output with `print()`

---

## Key Takeaways

- The `=` operator assigns values to variables.
- Variables can be reassigned as information changes.
- Strings store text.
- Lists store multiple values.
- Integers store whole numbers.
- Booleans store `True` or `False`.
- The `type()` function identifies an object's data type.
- Comparison operators return Boolean results.
- The `print()` function displays values and expressions.

---

## Skills Practiced

- Python Variables
- Python Data Types
- Lists
- Boolean Logic
- Comparison Operators
- Login Monitoring Concepts
- Basic Security Automation
