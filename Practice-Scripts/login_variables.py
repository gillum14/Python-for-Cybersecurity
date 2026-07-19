"""Demonstrate Python variables and data types in a login-monitoring scenario."""

DEVICE_ID = "72e08x0"
MAX_LOGINS = 3

approved_users = [
    "madebowa",
    "jnguyen",
    "tbecker",
    "nhersh",
    "redwards",
]

# Add a newly approved user without rebuilding the entire list.
approved_users.append("lpope")

login_attempts = 4
login_status = False

attempts_within_limit = login_attempts <= MAX_LOGINS

print("Device ID:", DEVICE_ID)
print("Device ID type:", type(DEVICE_ID).__name__)
print("Approved users:", approved_users)
print("Approved users type:", type(approved_users).__name__)
print("Maximum login attempts:", MAX_LOGINS)
print("Current login attempts:", login_attempts)
print("Attempts within limit:", attempts_within_limit)
print("Login status:", login_status)
print("Login status type:", type(login_status).__name__)
