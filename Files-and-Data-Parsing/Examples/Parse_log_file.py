with open("login.txt", "r") as file:
    text = file.read()

entries = text.split()

print(entries)
