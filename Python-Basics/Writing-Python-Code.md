# Writing Python Code

## Overview

Python is a widely used programming language that supports automation, data analysis, security monitoring, and incident response.

This exercise introduced the structure of Python notebooks, code cells, Markdown cells, comments, strings, and the `print()` function.

---

## Why It Matters

Security analysts use Python to automate repetitive tasks, process security data, analyze logs, and create tools that improve investigation efficiency.

Before developing security automation scripts, analysts need to understand how Python code is written, documented, and executed.

---

## Notebook Environments

A notebook environment allows code and documentation to appear together in the same file.

Notebooks typically contain two types of cells:

- Markdown cells
- Code cells

### Markdown Cells

Markdown cells contain formatted text rather than executable Python code.

They can be used to:

- Add headings
- Explain code
- Document findings
- Add instructions
- Include links
- Organize analysis

Example:

```markdown
# Security Analysis

This notebook analyzes authentication activity.
```

### Code Cells

Code cells contain executable Python code.

Example:

```python
print("Hello world!")
```

Output:

```text
Hello world!
```

In many notebook environments, a code cell can be executed using:

```text
Shift + Enter
```

---

## Python Comments

Comments document what code does and why it was written.

Python comments begin with the hash symbol (`#`).

```python
# This cell displays a message
print("I am using Python.")
```

Comments are ignored by the Python interpreter and do not appear in program output.

### Example

```python
# This code contains only comments
# Python will not display any output
```

Output:

```text
No output
```

---

## Why Comments Matter

Well-written comments help:

- Explain technical decisions
- Document security logic
- Make code easier to review
- Support team collaboration
- Simplify troubleshooting
- Preserve context for future updates

Comments should explain the purpose or reasoning behind code rather than repeat exactly what the code already says.

### Less Useful Comment

```python
# Print the word alert
print("Alert")
```

### More Useful Comment

```python
# Notify the analyst when suspicious activity is detected
print("Suspicious activity detected")
```

---

## The `print()` Function

The `print()` function displays information on the screen.

### Syntax

```python
print(value)
```

### Display a String

```python
print("I am a security analyst.")
```

Output:

```text
I am a security analyst.
```

The quotation marks identify the value as a string, but they are not included in the displayed output.

---

## Printing Multiple Statements

Python executes code from top to bottom.

```python
print("Hello world!")
print("I am using Python.")
print("I am a security analyst.")
print("Python is useful for security!")
```

Output:

```text
Hello world!
I am using Python.
I am a security analyst.
Python is useful for security!
```

Each `print()` statement produces a new line of output.

---

## Strings

A string is a sequence of characters enclosed in quotation marks.

Examples:

```python
"Hello world!"
```

```python
"I am a security analyst."
```

```python
"Python is useful for security!"
```

Python supports both single and double quotation marks:

```python
print("Security alert")
print('Security alert')
```

Both statements produce the same output.

---

## Code Execution Order

Python generally executes instructions:

1. From top to bottom
2. From left to right

Example:

```python
print("First")
print("Second")
print("Third")
```

Output:

```text
First
Second
Third
```

Understanding execution order becomes especially important when working with variables, conditions, loops, and functions.

---

## Cybersecurity Example

```python
# Display the status of a security investigation
print("Security investigation started")
print("Reviewing authentication logs")
print("Investigation complete")
```

Output:

```text
Security investigation started
Reviewing authentication logs
Investigation complete
```

This same concept can later be used to display:

- Alert messages
- Investigation status
- Login results
- File-processing updates
- Error notifications
- Script completion messages

---

## Lab Summary

During this lab, I practiced:

- Working in a notebook environment
- Using Markdown cells
- Running Python code cells
- Writing Python comments
- Displaying strings with `print()`
- Executing multiple statements
- Understanding Python execution order

---

## Key Takeaways

- Markdown cells contain formatted documentation.
- Code cells contain executable Python code.
- Python comments begin with `#`.
- Comments are ignored by the Python interpreter.
- The `print()` function displays information.
- Quotation marks define strings but do not appear in printed output.
- Python executes statements from top to bottom.
- Clear comments improve readability and collaboration.

---

## Skills Practiced

- Python Syntax
- Notebook Environments
- Markdown Documentation
- Code Comments
- Strings
- Output Formatting
- Technical Documentation
