approved_users = {
    "elarson": "8rp2k75",
    "bmoreno": "hl0s5o1",
    "sgilmore": "4n482ts",
    "eraab": "a307vir",
    "gesparza": "3rcv4w6"
}


def login(username, device_id):

    if username not in approved_users:
        print(f"{username} is NOT approved.")
        return

    print(f"{username} is approved.")

    if approved_users[username] == device_id:
        print("Correct assigned device.")
    else:
        print("Incorrect assigned device.")


login("sgilmore", "4n482ts")
login("sgilmore", "1111111")
login("hacker", "1234567")
