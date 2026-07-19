def update_file(import_file, remove_list):
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    ip_addresses = ip_addresses.split()

    for ip in ip_addresses:
        if ip in remove_list:
            ip_addresses.remove(ip)

    updated_ips = " ".join(ip_addresses)

    with open(import_file, "w") as file:
        file.write(updated_ips)


remove_list = [
    "192.168.25.60",
    "192.168.140.81",
    "192.168.203.198"
]

update_file("allow_list.txt", remove_list)
