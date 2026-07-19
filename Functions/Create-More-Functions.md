# Creating More Functions in Python

## Overview

Functions can accept data as input, process that data, and either display information or return a result that can be used elsewhere in a program.

This lab expands on basic function creation by introducing:

- Built-in functions
- Function parameters
- Return values
- Basic calculations
- Security-related login analysis

---

## Why It Matters

Security analysts frequently automate repetitive analysis such as:

- Counting failed logins
- Detecting abnormal authentication activity
- Calculating login trends
- Identifying suspicious behavior
- Triggering alerts based on thresholds

Functions allow these tasks to be reused throughout larger automation scripts.

---

# Built-in Functions

Python includes many useful built-in functions.

## sorted()

Returns a sorted copy of a list.

```python
failed_logins = [119, 101, 99, 91]

print(sorted(failed_logins))
```

Output

```
[91, 99, 101, 119]
```

---

## max()

Returns the largest value in a collection.

```python
failed_logins = [119, 101, 99, 264]

print(max(failed_logins))
```

Output

```
264
```

---

# Functions with Parameters

Functions become much more useful when they accept data.

Example

```python
def analyze_logins(username, current_day_logins):

    print("Current day login total for", username, "is", current_day_logins)
```

Calling the function

```python
analyze_logins("ejones", 9)
```

Output

```
Current day login total for ejones is 9
```

---

# Multiple Parameters

Functions can accept multiple inputs.

```python
def analyze_logins(username, current_day_logins, average_day_logins):

    print("Current day login total for", username, "is", current_day_logins)

    print("Average logins per day for", username, "is", average_day_logins)
```

---

# Calculations Inside Functions

Functions can perform calculations before producing output.

```python
login_ratio = current_day_logins / average_day_logins
```

Example

```
Current Day = 9
Average = 3

Ratio = 3.0
```

---

# Returning Values

Instead of printing information, functions can return data.

```python
def analyze_logins(username, current_day_logins, average_day_logins):

    login_ratio = current_day_logins / average_day_logins

    return login_ratio
```

The returned value can be stored.

```python
result = analyze_logins("ejones", 9, 3)
```

---

# Using Returned Values

Returned values can be used elsewhere.

```python
login_analysis = analyze_logins("ejones", 9, 3)

if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")
```

Output

```
Alert! This account has more login activity than normal.
```

---

# Security Applications

Functions like these can help automate:

- Login monitoring
- Brute-force detection
- Failed authentication analysis
- User activity reporting
- Threshold-based alerting
- SOC automation

---

# Lab Summary

During this lab I practiced:

- Using built-in functions
- Sorting data
- Finding maximum values
- Writing parameterized functions
- Returning values
- Reusing function output
- Triggering alerts with conditional logic

---

# Key Takeaways

- `sorted()` returns a sorted list.
- `max()` returns the largest value.
- Functions can accept parameters.
- Functions can perform calculations.
- `return` sends information back to the caller.
- Returned values can be used in additional logic.

---

## Skills Practiced

- Python
- Functions
- Parameters
- Return Statements
- Built-in Functions
- Automation
- Security Monitoring
