# Syntax Error Example

# Incorrect
# for i in range(5)
#     print(i)

# Correct
for i in range(5):
    print(i)

print()

# Exception Example

usernames = [
    "alice",
    "bob",
    "charlie"
]

print(usernames[2])

print()

# Logic Error Example

patch_schedule = [
    "March 1st",
    "April 1st",
    "May 1st"
]

system = "OS 2"

if system == "OS 1":
    print(patch_schedule[0])

elif system == "OS 2":
    print(patch_schedule[1])

elif system == "OS 3":
    print(patch_schedule[2])
