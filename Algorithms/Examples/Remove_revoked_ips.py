allow_list = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30"
]

remove_list = [
    "192.168.1.20"
]

updated_list = [ip for ip in allow_list if ip not in remove_list]

print(updated_list)
