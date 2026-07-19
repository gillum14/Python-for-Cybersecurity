# Loops in Python

## Overview

Loops allow repetitive tasks to be automated by executing the same block of code multiple times.

For cybersecurity professionals, loops are essential because analysts frequently need to process large amounts of data such as:

- Login attempts
- IP addresses
- User accounts
- Event logs
- Security alerts
- Devices on a network

Rather than writing the same code repeatedly, loops automate repetitive tasks efficiently.

---

## Why It Matters

Security analysts regularly work with hundreds or thousands of records.

Examples include:

- Reviewing login attempts
- Checking IP addresses against allow lists
- Processing event logs
- Creating user accounts
- Automating repetitive administrative tasks

Loops dramatically reduce manual effort while improving consistency.

---

# for Loops

A `for` loop repeats a block of code a specified number of times or iterates through every item in a collection.

## Syntax

```python
for item in sequence:
    statement
```

### Example

```python
for i in range(3):
    print("Connection could not be established.")
```

Output

```
Connection could not be established.
Connection could not be established.
Connection could not be established.
```

---

# Using range()

The `range()` function generates a sequence of numbers.

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

## Using Variables with range()

```python
connection_attempts = 3

for i in range(connection_attempts):
    print("Connection could not be established.")
```

This allows the number of loop iterations to change dynamically.

---

# while Loops

A `while` loop continues executing until a condition becomes False.

## Syntax

```python
while condition:
    statement
```

Example

```python
connection_attempts = 0

while connection_attempts < 3:
    print("Connection could not be established.")
    connection_attempts += 1
```

---

## for vs while

### Use a for loop when:

- Number of iterations is known
- Processing lists
- Reading files
- Looping through records

### Use a while loop when:

- Stopping condition is unknown
- Waiting for user input
- Monitoring events
- Polling systems

---

# Looping Through Lists

Lists are commonly processed one item at a time.

Example

```python
ip_addresses = [
    "192.168.142.245",
    "192.168.109.50",
    "192.168.86.232"
]

for ip in ip_addresses:
    print(ip)
```

---

# Combining Loops with Conditionals

Loops become much more powerful when paired with `if` statements.

Example

```python
for ip in ip_addresses:

    if ip in allow_list:
        print("IP address is allowed")

    else:
        print("IP address is not allowed")
```

This is a common Blue Team workflow.

---

# break

The `break` statement immediately exits a loop.

Example

```python
for ip in ip_addresses:

    if ip not in allow_list:
        print("Unauthorized IP detected")
        break
```

Useful when a security event requires immediate investigation.

---

# Generating Sequential Values

Loops can generate IDs automatically.

Example

```python
i = 5000

while i <= 5150:
    print(i)
    i += 5
```

Output

```
5000
5005
5010
...
5150
```

---

# Conditional Logic Inside Loops

Conditions can trigger alerts during iteration.

Example

```python
while i <= 5150:

    print(i)

    if i == 5100:
        print("Only 10 valid employee IDs remaining")

    i += 5
```

---

# Security Applications

Loops are commonly used for:

- Reviewing login attempts
- Checking allow lists
- Processing firewall logs
- Parsing SIEM alerts
- Enumerating devices
- Password auditing
- User management
- Threat hunting
- Automation scripts

---

# Lab Summary

During this lab I practiced:

- for loops
- while loops
- range()
- list iteration
- conditional logic inside loops
- break statements
- generating sequential IDs
- security automation workflows

---

# Key Takeaways

- `for` loops iterate through sequences.
- `while` loops repeat until a condition changes.
- `range()` controls loop iterations.
- Loops often work together with conditional statements.
- `break` immediately exits a loop.
- Loops are foundational for automation in cybersecurity.

---

## Skills Practiced

- Python
- Loops
- Automation
- Network Analysis
- Access Control
- Security Monitoring
- Blue Team Fundamentals
