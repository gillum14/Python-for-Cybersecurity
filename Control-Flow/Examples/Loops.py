"""
Loops Lab

Demonstrates:
- for loops
- while loops
- range()
- list iteration
- break
- security automation
"""

# ------------------------------------
# Repeating Connection Attempts
# ------------------------------------

print("=== Connection Attempts ===")

for i in range(3):
    print("Connection could not be established.")

print()

# ------------------------------------
# Variable Controlled Loop
# ------------------------------------

connection_attempts = 3

print("=== Variable Loop ===")

for i in range(connection_attempts):
    print("Connection could not be established.")

print()

# ------------------------------------
# While Loop
# ------------------------------------

print("=== While Loop ===")

connection_attempts = 0

while connection_attempts < 3:
    print("Connection could not be established.")
    connection_attempts += 1

print()

# ------------------------------------
# Loop Through IP Addresses
# ------------------------------------

ip_addresses = [
    "192.168.142.245",
    "192.168.109.50",
    "192.168.86.232",
    "192.168.131.147",
    "192.168.205.12",
    "192.168.200.48"
]

print("=== Login Attempts ===")

for ip in ip_addresses:
    print(ip)

print()

# ------------------------------------
# Allow List Check
# ------------------------------------

allow_list = [
    "192.168.243.140",
    "192.168.205.12",
    "192.168.151.162",
    "192.168.178.71",
    "192.168.86.232",
    "192.168.3.24",
    "192.168.170.243",
    "192.168.119.173"
]

print("=== Allow List Check ===")

for ip in ip_addresses:

    if ip in allow_list:
        print(f"{ip} -> Allowed")

    else:
        print(f"{ip} -> Not Allowed")

print()

# ------------------------------------
# Stop on Unauthorized Access
# ------------------------------------

print("=== Security Investigation ===")

for ip in ip_addresses:

    if ip in allow_list:
        print(f"{ip} -> Allowed")

    else:
        print(f"{ip} -> Unauthorized. Investigation Required.")
        break

print()

# ------------------------------------
# Employee ID Generator
# ------------------------------------

print("=== Employee IDs ===")

employee_id = 5000

while employee_id <= 5150:

    print(employee_id)

    if employee_id == 5100:
        print("Only 10 valid employee IDs remaining.")

    employee_id += 5
