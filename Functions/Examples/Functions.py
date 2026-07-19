"""
Functions Lab

Demonstrates:
- defining functions
- calling functions
- loops inside functions
- string concatenation
"""

# ---------------------------------------
# Basic Alert Function
# ---------------------------------------

def alert():
    print("Potential security issue. Investigate further.")

print("=== Basic Function ===")
alert()

print()

# ---------------------------------------
# Function with Loop
# ---------------------------------------

def repeated_alert():

    for i in range(3):
        print("Potential security issue. Investigate further.")

print("=== Repeated Alert ===")
repeated_alert()

print()

# ---------------------------------------
# Display Usernames
# ---------------------------------------

def display_usernames():

    username_list = [
        "elarson",
        "bmoreno",
        "tshah",
        "sgilmore",
        "eraab",
        "gesparza",
        "alevitsk",
        "wjaffrey"
    ]

    for username in username_list:
        print(username)

print("=== Approved Users ===")
display_usernames()

print()

# ---------------------------------------
# Convert List to String
# ---------------------------------------

def list_to_string():

    username_list = [
        "elarson",
        "bmoreno",
        "tshah",
        "sgilmore",
        "eraab",
        "gesparza",
        "alevitsk",
        "wjaffrey"
    ]

    combined = ""

    for username in username_list:
        combined += username + ", "

    print(combined)

print("=== Combined Username List ===")
list_to_string()
