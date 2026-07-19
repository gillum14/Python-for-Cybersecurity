# Read a security log file

with open("login.txt", "r") as file:
    log_contents = file.read()

print(log_contents)
