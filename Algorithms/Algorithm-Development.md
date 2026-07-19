# Develop an Algorithm

## Overview

Security analysts frequently automate repetitive tasks.

One common task is verifying:

- whether a user is approved
- whether they possess the correct assigned device

This lab demonstrates how Python lists, conditionals, indexing, and functions work together to build a simple authentication algorithm.

---

# Why It Matters

Organizations maintain:

- approved user lists
- assigned company devices
- inventory databases

Automation allows analysts to quickly verify that:

- a user exists
- the device belongs to them
- unauthorized users are denied access

This same concept is used in:

- Identity & Access Management (IAM)
- Endpoint Management
- Asset Inventory Systems
- Security Automation

---

# Synchronized Lists

Two lists can store related information.

```python
approved_users = [
    "elarson",
    "bmoreno",
    "tshah"
]

approved_devices = [
    "8rp2k75",
    "hl0s5o1",
    "2ye3lzg"
]
```

Each user corresponds to the device at the same index.

```
Index 0

elarson

↓

8rp2k75
```

---

# Accessing List Elements

```python
print(approved_users[0])
print(approved_devices[0])
```

Output

```
elarson
8rp2k75
```

---

# Adding New Users

Use `.append()`.

```python
approved_users.append("gesparza")
approved_devices.append("3rcv4w6")
```

Adds new elements to the end of each list.

---

# Removing Users

Use `.remove()`.

```python
approved_users.remove("tshah")
approved_devices.remove("2ye3lzg")
```

---

# Membership Testing

Use the `in` operator.

```python
if username in approved_users:
    print("Approved")
```

---

# Finding an Index

Use `.index()`.

```python
ind = approved_users.index(username)
```

Example

```
approved_users

0
1
2

elarson
bmoreno
sgilmore
```

```
approved_users.index("sgilmore")

returns

2
```

---

# Connecting Two Lists

Once the index is known:

```python
device = approved_devices[ind]
```

The matching device can be retrieved instantly.

---

# Comparing Devices

```python
if device_id == approved_devices[ind]:
    print("Correct device")
```

---

# Multiple Conditions

```python
if username in approved_users and device_id == approved_devices[ind]:
```

Both conditions must evaluate to True.

---

# Functions

Instead of repeating code:

```python
def login(username, device_id):
```

A function creates reusable logic.

The function:

- checks the username
- verifies the assigned device
- prints the appropriate response

---

# Algorithm Flow

```
User enters:

Username
Device ID

        │
        ▼

Is username approved?

        │
   Yes / No

        │
        ▼

Find user's index

        │
        ▼

Retrieve assigned device

        │
        ▼

Does device match?

        │
   Yes / No

        │
        ▼

Grant / Deny
```

---

# Security Applications

This same workflow appears in:

- Badge access systems
- Device inventory
- MFA enrollment
- Endpoint verification
- IAM platforms
- Asset management

---

# Skills Practiced

- Lists
- Indexing
- Membership testing
- append()
- remove()
- index()
- Functions
- Nested conditionals
- Algorithm development

---

# Key Takeaways

- Lists can store related information.
- Indexes connect related datasets.
- `.append()` adds items.
- `.remove()` deletes items.
- `.index()` locates an item.
- Functions make code reusable.
- Nested conditionals allow complex decision making.
