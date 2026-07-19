allowed_ips = """
192.168.218.160
192.168.97.225
192.168.145.158
192.168.108.13
"""

with open("allow_list.txt", "w") as file:
    file.write(allowed_ips)

print("Allow list created.")
