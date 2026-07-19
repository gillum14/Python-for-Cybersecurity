# Defining and Calling Functions in Python

## Overview

Functions allow code to be grouped into reusable blocks that can be executed whenever needed.

Instead of rewriting the same code multiple times, a function allows it to be defined once and called whenever required.

Functions are one of the most important programming concepts because they improve:

- Readability
- Reusability
- Organization
- Automation
- Scalability

---

## Why It Matters

Cybersecurity professionals frequently automate repetitive tasks such as:

- Generating alerts
- Reviewing logs
- Parsing files
- Processing user accounts
- Validating IP addresses
- Checking security configurations

Functions make these automations easier to manage and maintain.

---

# Defining a Function

Functions are created using the `def` keyword.

## Syntax

```python
def function_name():
    statement
```

Example

```python
def alert():
    print("Potential security issue. Investigate further.")
```

At this point the function exists, but nothing happens until it is called.

---

# Calling a Function

A function executes when its name is followed by parentheses.

```python
alert()
```

Output

```
Potential security issue. Investigate further.
```

---

# Reusing Functions

Functions can be called as many times as needed.

```python
alert()
alert()
alert()
```

Output

```
Potential security issue. Investigate further.
Potential security issue. Investigate further.
Potential security issue. Investigate further.
```

---

# Using Loops Inside Functions

Functions often contain loops.

Example

```python
def alert():

    for i in range(3):
        print("Potential security issue. Investigate further.")
```

Calling

```python
alert()
```

Output

```
Potential security issue. Investigate further.
Potential security issue. Investigate further.
Potential security issue. Investigate further.
```

---

# Functions Can Process Data

Functions commonly work with variables and collections.

Example

```python
def list_usernames():

    usernames = [
        "elarson",
        "bmoreno",
        "tshah"
    ]

    for username in usernames:
        print(username)
```

---

# String Concatenation

Strings can be combined using the `+` operator.

Example

```python
first = "Security"
second = "Operations"

result = first + second
```

Output

```
SecurityOperations
```

---

# Improving Readability

Adding separators makes concatenated strings easier to read.

Example

```python
usernames = [
    "elarson",
    "bmoreno",
    "tshah"
]

combined = ""

for username in usernames:
    combined += username + ", "

print(combined)
```

Output

```
elarson, bmoreno, tshah,
```

---

# Security Applications

Functions are commonly used to automate:

- Alert generation
- Log analysis
- Threat detection
- User management
- File parsing
- Network monitoring
- Authentication checks
- Compliance reporting

---

# Lab Summary

During this lab I practiced:

- Defining functions
- Calling functions
- Organizing reusable code
- Using loops inside functions
- Iterating through lists
- String concatenation
- Building reusable security utilities

---

# Key Takeaways

- Functions organize reusable code.
- Functions are defined with `def`.
- Parentheses execute a function.
- Functions can contain loops and conditional statements.
- String concatenation combines multiple strings.
- Functions are fundamental to automation in cybersecurity.

---

## Skills Practiced

- Python
- Functions
- Automation
- Code Reusability
- String Manipulation
- Security Scripting
