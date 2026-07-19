allow_list = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30"
]

remove_list = [
    "192.168.1.20",
    "192.168.1.50"
]

for ip in allow_list:
    if ip in remove_list:
        print(f"Remove: {ip}")
