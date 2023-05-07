import json
from remember_me import greet_user as gu
filename = "username.json"

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

gu()

