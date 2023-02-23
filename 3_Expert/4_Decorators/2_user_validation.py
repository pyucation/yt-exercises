"""
Topic: Decorators
Difficulty: 4/5
Requires: functions, closures

Task:
Imagine having a file with top-secret content in it. So far everyone could
open this file via the function 'open_resource' provided below.
Now, you are given two users. One of them is allowed to access the file and
one is not. Write a decorator ensuring that only admins can access the
top-secret file.
The function 'get_user' mimics a function providing specific user information
as 'get_jwt' in flask or some OS functionalities. To make it more interesting,
it chooses the user at random.
"""

import random


user1 = {
    "name": "Alice",
    "role": "Admin"
}

user2 = {
    "name": "Bob",
    "role": "User"
}


def get_user():
    return random.choice((user1, user2))


def open_resource(path):
    with open(path, 'r') as f:
        top_secret = f.read()
    return top_secret
