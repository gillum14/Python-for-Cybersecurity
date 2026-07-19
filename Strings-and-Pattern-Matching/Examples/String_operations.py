"""
Working with Strings

Demonstrates:

- str()
- len()
- concatenation
- indexing
- slicing
- index()
"""

# ------------------------
# Employee ID
# ------------------------

employee_id = 4186

print(type(employee_id))

employee_id = str(employee_id)

print(type(employee_id))

# ------------------------
# Validate ID Length
# ------------------------

if len(employee_id) < 5:
    print("Employee ID does not meet length requirements.")

# ------------------------
# Standardize ID
# ------------------------

employee_id = "E" + employee_id

print(employee_id)

# ------------------------
# Device ID
# ------------------------

device_id = "r262c36"

print("Fourth character:", device_id[3])

print("First three characters:", device_id[0:3])

# ------------------------
# URL Parsing
# ------------------------

url = "https://exampleURL1.com"

print("Protocol:", url[0:8])

extension_index = url.index(".com")

print("Extension:", url[extension_index:extension_index+4])

print("Website:", url[8:extension_index])
