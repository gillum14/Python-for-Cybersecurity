usernames = [
    "alice",
    "bob",
    "charlie"
]

try:
    print(usernames[5])

except IndexError:
    print("Index out of range.")
