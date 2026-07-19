"""
Conditional Statements Lab

Demonstrates Python decision-making using:
- if
- elif
- else
- and
- or
- in
"""

# -------------------------------
# Operating System Check
# -------------------------------

system = "OS 3"

if system == "OS 2":
    print("No update needed.")
elif system == "OS 1" or system == "OS 3":
    print("Update needed.")
else:
    print("Unknown operating system.")

print()

# -------------------------------
# Approved User Check
# -------------------------------

approved_users = [
    "elarson",
    "bmoreno",
    "tshah",
    "sgilmore",
    "eraab"
]

username = "bmoreno"

if username in approved_users:
    print("User is authorized.")
else:
    print("User is NOT authorized.")

print()

# -------------------------------
# Organization Hours Check
# -------------------------------

organization_hours = True

if organization_hours:
    print("Login occurred during organization hours.")
else:
    print("Login occurred outside organization hours.")

print()

# -------------------------------
# Combined Security Check
# -------------------------------

if username in approved_users and organization_hours:
    print("Approved login during organization hours.")
else:
    print("Login denied.")
