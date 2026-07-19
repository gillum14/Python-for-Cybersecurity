"""
Develop an Algorithm

User / Device Verification
"""

approved_users = [
    "elarson",
    "bmoreno",
    "sgilmore",
    "eraab",
    "gesparza"
]

approved_devices = [
    "8rp2k75",
    "hl0s5o1",
    "4n482ts",
    "a307vir",
    "3rcv4w6"
]


def login(username, device_id):

    if username in approved_users:

        print(f"{username} is approved.")

        index = approved_users.index(username)

        if device_id == approved_devices[index]:
            print(f"{device_id} is assigned to {username}")

        else:
            print(f"{device_id} is NOT assigned to {username}")

    else:
        print(f"{username} is NOT approved.")


login("bmoreno", "hl0s5o1")
login("elarson", "r2s5r9g")
login("abernard", "4n482ts")
