"""
Topic: if statements
Difficulty: 2/5
Requires: basic datatypes

Task:
You are given a small vending machine in form of a dictionary and another
dictionary that maps a user input to the item (so that we can write "1"
instead of "coke"). Design a mechanism that prevents customers under 18 from
buying cigaretts and alcohol. Additionally, check if the person has enough
money to buy a product.
"""

prices = {
    "coke": 1.20,
    "cigarettes": 5.80,
    "sandwich": 2.40,
    "water": 0.90,
    "beer": 1.80
}

items = {
    "1": "coke",
    "2": "cigarettes",
    "3": "sandwich",
    "4": "water",
    "5": "beer"
}

# your money
money = 3.2

print("Welcome to AVen - Awesome Vending Machines!")
try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("This is not a valid age.")

print("What do you want to buy?")
print("1 - coke\n2 - cigarettes\n3 - sandwich\n4 - water\n5 - beer")
choice = input("Please enter your choice: ")


# ENTER YOUR CODE HERE
