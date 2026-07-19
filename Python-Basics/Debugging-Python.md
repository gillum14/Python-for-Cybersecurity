# Debug Python Code

## Overview

Writing code is only part of programming. Security analysts must also identify, troubleshoot, and correct errors to ensure automation scripts function reliably.

This lab focused on recognizing and resolving common Python errors, including syntax errors, exceptions, and logic errors.

---

# Why It Matters

Automation is only valuable if it works correctly.

Debugging helps security analysts:

- Correct broken automation
- Improve reliability
- Prevent inaccurate results
- Reduce downtime
- Troubleshoot security scripts

---

# Types of Errors

## Syntax Errors

Syntax errors occur when Python cannot understand the code.

Examples:

- Missing colon (`:`)
- Missing quotation mark
- Missing parenthesis
- Missing comma
- Incorrect indentation

Example:

```python
for i in range(10)
    print(i)
```

Correct:

```python
for i in range(10):
    print(i)
```

---

## Exceptions

Exceptions occur while the program is running.

Common examples include:

- IndexError
- NameError
- TypeError
- AttributeError
- FileNotFoundError

Example:

```python
numbers = [1,2,3]

print(numbers[5])
```

Produces:

```
IndexError
```

---

## Logic Errors

Logic errors allow the code to run successfully but produce incorrect results.

Example:

```python
patch_schedule = [
    "March",
    "April",
    "May"
]

system = "OS 2"

print(patch_schedule[0])
```

Runs successfully but returns the wrong patch date.

---

# Debugging Process

A good debugging workflow:

1. Read the error message.
2. Identify the line causing the error.
3. Correct one issue at a time.
4. Run the code again.
5. Verify the output.

---

# Common Errors Fixed

## Missing Colon

```python
if user == "admin"
```

Correct:

```python
if user == "admin":
```

---

## Missing Parenthesis

```python
print("Hello"
```

Correct:

```python
print("Hello")
```

---

## Incorrect Comparison

Incorrect:

```python
if user = "admin":
```

Correct:

```python
if user == "admin":
```

---

## Incorrect Method Call

Incorrect:

```python
split.ip_addresses()
```

Correct:

```python
ip_addresses.split()
```

---

## Incorrect List Index

Incorrect:

```python
usernames[5]
```

Correct:

```python
usernames[4]
```

---

# Security Applications

Debugging is critical for:

- Security automation
- Log parsing
- Threat detection scripts
- Incident response automation
- File parsing
- API integrations
- Cloud security tooling

---

# Skills Practiced

- Reading error messages
- Fixing syntax errors
- Resolving exceptions
- Correcting logic errors
- Testing code
- Verifying expected output

---

# Key Takeaways

- Python stops at the first error it encounters.
- Fix one error at a time.
- Syntax errors prevent execution.
- Exceptions occur while running code.
- Logic errors produce incorrect results despite successful execution.
- Always test your code after making changes.
