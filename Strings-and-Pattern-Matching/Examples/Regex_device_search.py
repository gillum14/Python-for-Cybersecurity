import re

devices = """
r262c36
67bv8fy
41j1u2e
r151dm4
1270t3o
r15xk9h
r15u9q5
r159r1u
"""

pattern = r"r15\w+"

matches = re.findall(pattern, devices)

print(matches)
