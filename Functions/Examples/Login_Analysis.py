"""
Login Analysis Lab

Demonstrates:
- built-in functions
- parameters
- return values
- login analysis
"""

# -------------------------------
# Failed login statistics
# -------------------------------

failed_login_list = [
    119,
    101,
    99,
    91,
    92,
    105,
    108,
    85,
    88,
    90,
    264,
    223
]

print("Sorted Login Attempts:")
print(sorted(failed_login_list))

print()

print("Highest Login Attempts:")
print(max(failed_login_list))

print()

# -------------------------------
# Login Analysis Function
# -------------------------------

def analyze_logins(username, current_day_logins, average_day_logins):

    print("Current day login total for", username, "is", current_day_logins)

    print("Average logins per day for", username, "is", average_day_logins)

    login_ratio = current_day_logins / average_day_logins

    return login_ratio


login_analysis = analyze_logins(
    "ejones",
    9,
    3
)

print()

print(
    "ejones logged in",
    login_analysis,
    "times as much as they do on an average day."
)

print()

if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")
