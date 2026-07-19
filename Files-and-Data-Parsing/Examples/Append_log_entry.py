# Append a new login entry

new_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09\n"

with open("login.txt", "a") as file:
    file.write(new_entry)

print("Log updated.")
